# `/setup-project` - Tự động Setup Project

## Mô tả
Tự động setup project hoàn chỉnh với structure chuẩn, README, package.json, scripts và git repository.

## Usage
```
/setup-project <project_name> [type]
```

## Parameters
- `project_name` (required): Tên project
- `type` (optional): Loại project (web, api, script, etc.)

## Workflow
1. Tạo project structure:
   - `src/` - Source code
   - `docs/` - Documentation
   - `scripts/` - Scripts
   - `configs/` - Configuration files
   - `tests/` - Test files

2. Tạo files:
   - `README.md` - Project documentation
   - `package.json` - Dependencies và scripts
   - `scripts/setup.sh` - Setup script

3. Init git:
   - Initialize git repository
   - Initial commit với message: "Initial commit: Auto-generated project by Ultimate Assistant"

## Examples
```
/setup-project my-web-app web
/setup-project api-service api
/setup-project automation-tool script
```

## Output
```
🚀 ĐANG SETUP PROJECT: [project_name]

📁 Đang tạo structure...
✅ src/ created
✅ docs/ created
✅ scripts/ created
✅ configs/ created
✅ tests/ created

📝 Đang tạo files...
✅ README.md created
✅ package.json created
✅ scripts/setup.sh created

🔧 Đang init git...
✅ Git repository initialized
✅ Initial commit created

✅ XONG: Project [project_name] đã sẵn sàng!
📁 Location: [path]
```

## Notes
- Sử dụng script: `scripts/auto-project-setup.sh`
- Tự động tạo structure chuẩn
- Tự động init git và commit
- Không hỏi lại, auto-run mode

