# HomeAssistant Automation UI 與 YAML 規則
| 建立方式                     | 儲存位置                 | UI 是否可見 | UI 編輯後存哪           |
| ------------------------ | -------------------- | ------- | ------------------ |
| UI 建立                    | `automations.yaml`   | ✅       | `automations.yaml` |
| YAML（automations.yaml）   | `automations.yaml`   | ✅       | `automations.yaml` |
| YAML（configuration.yaml） | `configuration.yaml` | ❌       | N/A                |

# 原則
- 手動檔案：
只在 YAML 寫
UI 只做「啟用 / 停用」

- UI automation：
完全不手動編輯, 以免UI出錯
也不要使用UI編輯 手動檔案。
UI 一旦編輯, 視為 HA 接管, 會移除註解, 簡化格式, 不易人類閱讀

# 目前架構
UI 使用 automations.yaml
自訂內容拆成獨立檔案, 放置於 automations 資料夾
```
/config/
├─ configuration.yaml
├─ automations.yaml          # UI 全權管理
└─ automations/
   ├─ lighting.yaml          # 手動
   ├─ climate.yaml           # 手動
   └─ security.yaml          # 手動
```
`configuration.yaml`
```yaml
automation:
  - !include automations.yaml           # UI 專用
  - !include_dir_merge_list automations # 手動專用
```
每個手動檔案須包含id, alias, 更容易分辨
```yaml
- id: core_livingroom_light
  alias: CORE|客廳燈光
  trigger:
    - platform: state
      entity_id: sensor.livingroom_motion
      to: "on"
  action:
    - service: light.turn_on
      target:
        entity_id: light.living_room
```
