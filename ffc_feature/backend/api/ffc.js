// Next.js API Route: app/api/ffc/route.js
import { NextResponse } from 'next/server'
import { getFirestore, collection, getDocs, doc, updateDoc, deleteDoc, addDoc, query, orderBy } from 'firebase-admin/firestore'
import { initializeApp, getApps, cert } from 'firebase-admin/app'

// Initialize Firebase Admin
if (!getApps().length) {
  initializeApp({
    credential: cert({
      projectId: process.env.FIREBASE_PROJECT_ID,
      clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
      privateKey: process.env.FIREBASE_PRIVATE_KEY?.replace(/\\n/g, '\n')
    })
  })
}

const db = getFirestore()

// GET - Get all feature flags
export async function GET(request) {
  try {
    const flagsRef = collection(db, 'featureFlags')
    const q = query(flagsRef, orderBy('updatedAt', 'desc'))
    const snapshot = await getDocs(q)
    
    const flags = snapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }))

    return NextResponse.json({ success: true, data: flags })
  } catch (error) {
    console.error('Error fetching flags:', error)
    return NextResponse.json(
      { success: false, error: error.message },
      { status: 500 }
    )
  }
}

// POST - Create new feature flag
export async function POST(request) {
  try {
    const body = await request.json()
    const { name, description, enabled = false, tags = [] } = body

    if (!name) {
      return NextResponse.json(
        { success: false, error: 'Name is required' },
        { status: 400 }
      )
    }

    const flagData = {
      name,
      description: description || '',
      enabled: Boolean(enabled),
      tags: Array.isArray(tags) ? tags : [],
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      createdBy: 'admin' // TODO: Get from session
    }

    const docRef = await addDoc(collection(db, 'featureFlags'), flagData)

    return NextResponse.json({
      success: true,
      data: { id: docRef.id, ...flagData }
    })
  } catch (error) {
    console.error('Error creating flag:', error)
    return NextResponse.json(
      { success: false, error: error.message },
      { status: 500 }
    )
  }
}

// PUT - Update feature flag
export async function PUT(request) {
  try {
    const body = await request.json()
    const { id, ...updates } = body

    if (!id) {
      return NextResponse.json(
        { success: false, error: 'ID is required' },
        { status: 400 }
      )
    }

    const flagRef = doc(db, 'featureFlags', id)
    await updateDoc(flagRef, {
      ...updates,
      updatedAt: new Date().toISOString()
    })

    return NextResponse.json({ success: true })
  } catch (error) {
    console.error('Error updating flag:', error)
    return NextResponse.json(
      { success: false, error: error.message },
      { status: 500 }
    )
  }
}

// DELETE - Delete feature flag
export async function DELETE(request) {
  try {
    const { searchParams } = new URL(request.url)
    const id = searchParams.get('id')

    if (!id) {
      return NextResponse.json(
        { success: false, error: 'ID is required' },
        { status: 400 }
      )
    }

    await deleteDoc(doc(db, 'featureFlags', id))

    return NextResponse.json({ success: true })
  } catch (error) {
    console.error('Error deleting flag:', error)
    return NextResponse.json(
      { success: false, error: error.message },
      { status: 500 }
    )
  }
}
