'use client'

import { useState, useEffect } from 'react'
import { collection, getDocs, doc, updateDoc, deleteDoc, addDoc, query, orderBy } from 'firebase/firestore'
import { db } from '@/lib/firebase'

interface FeatureFlag {
  id: string
  name: string
  description: string
  enabled: boolean
  createdAt: string
  updatedAt: string
  createdBy: string
  tags: string[]
  usage?: {
    enabledCount: number
    disabledCount: number
  }
}

export default function FFCDashboard() {
  const [flags, setFlags] = useState<FeatureFlag[]>([])
  const [loading, setLoading] = useState(true)
  const [showModal, setShowModal] = useState(false)
  const [editingFlag, setEditingFlag] = useState<FeatureFlag | null>(null)
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    enabled: false,
    tags: ''
  })

  useEffect(() => {
    loadFlags()
  }, [])

  const loadFlags = async () => {
    try {
      const flagsRef = collection(db, 'featureFlags')
      const q = query(flagsRef, orderBy('updatedAt', 'desc'))
      const snapshot = await getDocs(q)
      const flagsData = snapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      } as FeatureFlag))
      setFlags(flagsData)
    } catch (error) {
      console.error('Error loading flags:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleToggle = async (flag: FeatureFlag) => {
    try {
      const flagRef = doc(db, 'featureFlags', flag.id)
      await updateDoc(flagRef, {
        enabled: !flag.enabled,
        updatedAt: new Date().toISOString()
      })
      loadFlags()
    } catch (error) {
      console.error('Error toggling flag:', error)
      alert('Lỗi khi cập nhật flag')
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const flagData = {
        ...formData,
        tags: formData.tags.split(',').map(t => t.trim()).filter(t => t),
        createdAt: editingFlag ? editingFlag.createdAt : new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        createdBy: 'admin' // TODO: Get from auth
      }

      if (editingFlag) {
        const flagRef = doc(db, 'featureFlags', editingFlag.id)
        await updateDoc(flagRef, flagData)
      } else {
        await addDoc(collection(db, 'featureFlags'), flagData)
      }

      setShowModal(false)
      setEditingFlag(null)
      setFormData({ name: '', description: '', enabled: false, tags: '' })
      loadFlags()
    } catch (error) {
      console.error('Error saving flag:', error)
      alert('Lỗi khi lưu flag')
    }
  }

  const handleDelete = async (id: string) => {
    if (!confirm('Bạn có chắc muốn xóa feature flag này?')) return
    
    try {
      await deleteDoc(doc(db, 'featureFlags', id))
      loadFlags()
    } catch (error) {
      console.error('Error deleting flag:', error)
      alert('Lỗi khi xóa flag')
    }
  }

  const handleEdit = (flag: FeatureFlag) => {
    setEditingFlag(flag)
    setFormData({
      name: flag.name,
      description: flag.description,
      enabled: flag.enabled,
      tags: flag.tags.join(', ')
    })
    setShowModal(true)
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-xl">Đang tải...</div>
      </div>
    )
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Feature Flags Management</h1>
        <button
          onClick={() => {
            setEditingFlag(null)
            setFormData({ name: '', description: '', enabled: false, tags: '' })
            setShowModal(true)
          }}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          + Thêm Feature Flag
        </button>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div className="bg-white p-4 rounded shadow">
          <div className="text-gray-600">Tổng số Flags</div>
          <div className="text-2xl font-bold">{flags.length}</div>
        </div>
        <div className="bg-green-50 p-4 rounded shadow">
          <div className="text-green-700">Đang bật</div>
          <div className="text-2xl font-bold text-green-600">
            {flags.filter(f => f.enabled).length}
          </div>
        </div>
        <div className="bg-red-50 p-4 rounded shadow">
          <div className="text-red-700">Đang tắt</div>
          <div className="text-2xl font-bold text-red-600">
            {flags.filter(f => !f.enabled).length}
          </div>
        </div>
      </div>

      {/* Flags Table */}
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="min-w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tên</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Mô tả</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tags</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Trạng thái</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Thao tác</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {flags.map(flag => (
              <tr key={flag.id} className="hover:bg-gray-50">
                <td className="px-6 py-4 whitespace-nowrap font-medium">{flag.name}</td>
                <td className="px-6 py-4">{flag.description}</td>
                <td className="px-6 py-4">
                  <div className="flex gap-2">
                    {flag.tags.map(tag => (
                      <span key={tag} className="bg-gray-100 px-2 py-1 rounded text-xs">
                        {tag}
                      </span>
                    ))}
                  </div>
                </td>
                <td className="px-6 py-4">
                  <button
                    onClick={() => handleToggle(flag)}
                    className={`px-3 py-1 rounded text-sm font-medium ${
                      flag.enabled
                        ? 'bg-green-100 text-green-800'
                        : 'bg-red-100 text-red-800'
                    }`}
                  >
                    {flag.enabled ? 'Đang bật' : 'Đang tắt'}
                  </button>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <button
                    onClick={() => handleEdit(flag)}
                    className="text-blue-600 hover:text-blue-800 mr-4"
                  >
                    Sửa
                  </button>
                  <button
                    onClick={() => handleDelete(flag.id)}
                    className="text-red-600 hover:text-red-800"
                  >
                    Xóa
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {flags.length === 0 && (
          <div className="text-center py-12 text-gray-500">
            Chưa có feature flags. Hãy thêm flag đầu tiên!
          </div>
        )}
      </div>

      {/* Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 max-w-md w-full">
            <h2 className="text-2xl font-bold mb-4">
              {editingFlag ? 'Sửa Feature Flag' : 'Thêm Feature Flag'}
            </h2>
            <form onSubmit={handleSubmit}>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-1">Tên *</label>
                <input
                  type="text"
                  required
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="w-full border rounded px-3 py-2"
                  placeholder="vd: enable_new_ui"
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-1">Mô tả</label>
                <textarea
                  value={formData.description}
                  onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                  className="w-full border rounded px-3 py-2"
                  rows={3}
                  placeholder="Mô tả tính năng..."
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-1">Tags (phân cách bởi dấu phẩy)</label>
                <input
                  type="text"
                  value={formData.tags}
                  onChange={(e) => setFormData({ ...formData, tags: e.target.value })}
                  className="w-full border rounded px-3 py-2"
                  placeholder="vd: ui, experimental, payment"
                />
              </div>
              <div className="mb-4">
                <label className="flex items-center">
                  <input
                    type="checkbox"
                    checked={formData.enabled}
                    onChange={(e) => setFormData({ ...formData, enabled: e.target.checked })}
                    className="mr-2"
                  />
                  Bật ngay
                </label>
              </div>
              <div className="flex gap-2 justify-end">
                <button
                  type="button"
                  onClick={() => {
                    setShowModal(false)
                    setEditingFlag(null)
                  }}
                  className="px-4 py-2 border rounded hover:bg-gray-50"
                >
                  Hủy
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
                >
                  {editingFlag ? 'Cập nhật' : 'Tạo'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
