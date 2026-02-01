#!/bin/bash

# 定義 Home Assistant 設定路徑
CONFIG_DIR="/config"
cd $CONFIG_DIR

# --- 安全檢查 ---
if [ ! -f ".gitignore" ]; then
    echo "❌ 錯誤: 找不到 .gitignore 檔案！為了安全，請先建立它。" >&2
    exit 1
fi

if grep -q "secrets.yaml" ".gitignore"; then
    echo "✅ 安全檢查通過: secrets.yaml 已在忽略清單中。" >&2
else
    echo "❌ 警告: .gitignore 中未發現 secrets.yaml！請先加入以防洩密。" >&2
    exit 1
fi

# --- 執行 Git 操作 ---
echo "🔄 正在掃描變更..." >&2

# 檢查是否有變更需要提交
if [ -z "$(git status --porcelain)" ]; then
    echo "ℹ️ 沒有發現任何變更，不需要上傳。"
    exit 0
fi

# 獲取變更檔案數量
file_count=$(git status --porcelain | wc -l)
echo "📝 變更檔案數: $file_count" >&2

# 加入所有變更
git add .

# 設定 Commit 訊息 (如果有傳入參數就用參數，沒有就用時間戳記)
if [ -z "$1" ]; then
    COMMIT_MSG="HA Config Update - $(date +'%Y-%m-%d %H:%M:%S')"
else
    COMMIT_MSG="$1"
fi

echo "💾 正在提交變更: $COMMIT_MSG" >&2
if ! git commit -m "$COMMIT_MSG" 2>&1 | grep -v "^$" >&2; then
    echo "❌ Git commit 失敗" >&2
    exit 1
fi

# 獲取 commit hash
commit_hash=$(git rev-parse --short HEAD)
echo "📦 Commit: $commit_hash" >&2

# 推送到遠端
echo "🚀 正在推送到 GitHub..." >&2
if git push origin main 2>&1 | grep -v "^$" >&2; then
    # 成功：輸出摘要資訊到 stdout
    echo "✅ 成功推送 $file_count 個檔案 (Commit: $commit_hash)"
    exit 0
else
    echo "❌ 上傳失敗，請檢查網路或 PAT Token 設定。" >&2
    exit 1
fi