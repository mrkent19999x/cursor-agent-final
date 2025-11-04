# `/deploy` - Deploy Project Tự Động

## Mô tả
Deploy project tự động lên môi trường staging hoặc production.

## Usage
```
/deploy <project> [env]
```

## Parameters
- `project` (required): Tên project cần deploy
- `env` (optional): Môi trường (staging/production). Default: staging

## Workflow
1. **Check project:**
   - Verify project exists
   - Check project status

2. **Run tests:**
   - Run unit tests
   - Run integration tests
   - Check test results

3. **Build:**
   - Run build command (`npm run build`)
   - Check build status

4. **Deploy:**
   - Deploy to environment
   - Monitor deployment
   - Check deployment status

5. **Monitor:**
   - Monitor service status
   - Check logs
   - Generate report

6. **Notify:**
   - Send notification email (nếu có config)

## Output Format
```
🚀 ĐANG DEPLOY: [Project Name]

🧪 Running tests...
✅ Tests passed

🔨 Building...
✅ Build successful

📤 Deploying to [environment]...
✅ Deployment successful

📊 Monitoring...
✅ Service is running

✅ XONG: [Project Name] đã deploy thành công!
🌐 URL: [url]
```

## Examples
```
/deploy my-web-app staging
/deploy api-service production
/deploy automation-tool
```

## Notes
- **Sử dụng script:** `scripts/auto-deploy.sh <project_name>`
- **Error handling:** Check và fix errors
- **Status reporting:** Luôn báo kết quả rõ ràng
- **Auto-run mode:** Không hỏi lại, tự động làm

## Error Handling
- Nếu tests fail → Stop và báo lỗi
- Nếu build fail → Stop và báo lỗi
- Nếu deploy fail → Rollback và báo lỗi

