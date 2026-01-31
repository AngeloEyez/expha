#!/bin/bash

# 定義 Home Assistant 設定路徑
CONFIG_DIR="/config"
cd $CONFIG_DIR

# --- 安全檢查 ---
if [ ! -f ".gitignore" ]; then
    echo "❌ 錯誤: 找不到 .gitignore 檔案！為了安全，請先建立它。"
    exit 1
fi

if grep -q "secrets.yaml" ".gitignore"; then
    echo "✅ 安全檢查通過: secrets.yaml 已在忽略清單中。"
else
    echo "❌ 警告: .gitignore 中未發現 secrets.yaml！請先加入以防洩密。"
    exit 1
fi

# --- 執行 Git 操作 ---
echo "🔄 正在掃描變更..."

# 檢查是否有變更需要提交
if [ -z "$(git status --porcelain)" ]; then
    echo "ℹ️  沒有發現任何變更，不需要上傳。"
    exit 0
fi

# 加入所有變更
git add .

# 設定 Commit 訊息 (如果有傳入參數就用參數，沒有就用時間戳記)
if [ -z "$1" ]; then
    COMMIT_MSG="HA Config Update - $(date +'%Y-%m-%d %H:%M:%S')"
else
    COMMIT_MSG="$1"
fi

echo "💾 正在提交變更: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

# 推送到遠端
echo "🚀 正在推送到 GitHub..."
if git push origin main; then
    echo "🎉 上傳成功！"
else
    echo "❌ 上傳失敗，請檢查網路或 PAT Token 設定。"
    exit 1
fi