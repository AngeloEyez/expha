#!/bin/bash

# 定義 Home Assistant 設定路徑
CONFIG_DIR="/config"
cd $CONFIG_DIR

echo "🔄 開始同步雲端更新..."

# --- 安全檢查：檢查本地是否有未提交的變更 ---
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  警告: 本地有尚未提交的變更！"
    echo "為了避免衝突，請先執行 ./git_push.sh 或是手動處理變更。"
    exit 1
fi

# --- 執行 Git Pull ---
echo "📡 正在從 GitHub 抓取資料..."
if git pull origin main; then
    echo "🎉 同步完成！"
    
    # --- 自動化提示：檢查 YAML 語法 ---
    echo "🔍 正在檢查 Home Assistant 設定檔語法..."
    ha core check
else
    echo "❌ 同步失敗，請檢查網路連線或 PAT Token。"
    exit 1
fi

echo "💡 提示：如果更新了自動化或腳本，請記得在 HA 介面重新載入設定。"