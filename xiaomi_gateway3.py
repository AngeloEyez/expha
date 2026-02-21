# /config/xiaomi_gateway3.py
from custom_components.xiaomi_gateway3.core.devices import *

DEVICES = [{
    # Aqara D100 智能推拉鎖 (ZNMS20LM)
    # https://home.miot-spec.com/spec?type=urn:miot-spec-v2:device:lock:0000A038:lumi-bacn01:1
    3051: ["Aqara", "Door Lock D100", "ZNMS20LM", "lumi.lock.bacn01"],
    "spec": [
        # --- 藍牙廣播事件 (mibeacon) ---
        # 門鎖開關、指紋與解鎖狀態事件 (eid: 6, 7, 11)
        BLEFinger("fingerprint", mi=6),
        BLEDoor("door", mi=7),
        BLELock("lock", mi=11),
        # 藍牙狀態回報 (mi=4106 電池, mi=4110 鎖狀態, mi=4111 門狀態)
        BLEByteConv("battery", "sensor", mi=4106),
        BLEMapConv("lock", "binary_sensor", mi=4110, map={"00": True, "01": False}),
        BLEMapConv("door", "binary_sensor", mi=4111, map={"00": True, "01": False}),

        # --- 電池資訊 (SIID 4) ---
        # 4.p.1: 電池電量百分比 (0-100)
        BaseConv("battery", "sensor", mi="4.p.1"),

        # --- 門鎖狀態 (SIID 2) ---
        # 2.p.1: 操作方式 (0:藍牙外側, 1:密碼, 2:指紋, 4:鑰匙, 6:NFC, 7:一次性密碼, 9:手動外側, 10:手動內側, 11:自動)
        MapConv("method", "sensor", mi="2.p.1", map={0: "BLE Outdoor", 1: "Password", 2: "Fingerprint", 4: "Key", 6: "NFC", 7: "One-time Password", 9: "Manual Outdoor", 10: "Manual Indoor", 11: "Automatic"}),
        
        # 2.p.2: 操作者 ID
        BaseConv("key_id", "sensor", mi="2.p.2"),
        
        # 2.p.3: 門鎖異常狀態 (0:多次密碼錯誤, 1:多次指紋錯誤, 3:防撬報警, 8:未上鎖超時, 10:室內布防狀態下開鎖, 11:多次解鎖錯誤, 12:多次NFC錯誤, 16:指紋模組異常, 19:機械故障)
        MapConv("error", "sensor", mi="2.p.3", map={0: "Frequent Wrong Password", 1: "Frequent Wrong Fingerprint", 3: "Lockpicking", 8: "Timeout Not Locked", 10: "Arming State Unlocked Indoor", 11: "Frequent Wrong Unlock", 12: "Frequent Wrong NFC", 16: "Abnormal Fingerprint Sensor", 19: "Mechanical Fault"}),
        
        # --- 門狀態 (SIID 5) ---
        # 5.p.2: 門異常狀態 (0:開門, 2:開門超時)
        MapConv("door_error", "sensor", mi="5.p.2", map={0: "Open Door", 2: "Open Over Time"}),

        # --- 觸發事件 ---
        BaseConv("action", "sensor"),
        # 2.e.1: 開鎖
        ConstConv("action", mi="2.e.1", value="Lock Opened"),
        # 2.e.2: 上鎖
        ConstConv("action", mi="2.e.2", value="Lock Locked"),
        # 2.e.3: 反鎖
        ConstConv("action", mi="2.e.3", value="Back Locking"),
        # 2.e.4: 門鎖異常發生
        ConstConv("action", mi="2.e.4", value="Exception Occurred"),
        # 5.e.1: 門異常發生
        ConstConv("action", mi="5.e.1", value="Door Exception Occurred"),
        
        # --- 以下為騙過 UI 用的定義，不對應實體 mi 地址，僅供 UI 掃描 ---
        ConstConv("action", value="Lock Opened"),
        ConstConv("action", value="Lock Locked"),
        ConstConv("action", value="Back Locking"),
        ConstConv("action", value="Exception Occurred"),
        ConstConv("action", value="Door Exception Occurred"),
    ],
}, {
    # 领普智能墙壁开关（四键）
    # https://home.miot-spec.com/spec/linp.switch.t2dbw4
    26373: ["Linptech", "T2 4-Key Wall Switch", "linp.switch.t2dbw4"],
    "spec": [
        # --- 四路實體開關通道 ---
        BaseConv("switch_1", "switch", mi="2.p.1"),
        BaseConv("switch_2", "switch", mi="3.p.1"),
        BaseConv("switch_3", "switch", mi="4.p.1"),
        BaseConv("switch_4", "switch", mi="5.p.1"),

        # --- 無線開關模式 (True 為純無線, False 為有線+無線) ---
        MapConv("mode_1", "select", mi="2.p.2", map={0: "Wired", 1: "Wireless"}),
        MapConv("mode_2", "select", mi="3.p.2", map={0: "Wired", 1: "Wireless"}),
        MapConv("mode_3", "select", mi="4.p.2", map={0: "Wired", 1: "Wireless"}),
        MapConv("mode_4", "select", mi="5.p.2", map={0: "Wired", 1: "Wireless"}),

        # --- 按鍵動作感測器 ---
        # 根據 Log: siid 6, eiid 1。使用 .p.1 取得 arguments 參數
        # --- 按鍵動作感測器 (捕捉所有點擊類型) ---
        BaseConv("action", "sensor"),
        
        # siid 6, event 1=single, event 2=double, event 3=hold
        MapConv("action", mi="6.e.1.p.1", map={1: BUTTON_1_SINGLE, 2: BUTTON_2_SINGLE, 3: BUTTON_3_SINGLE, 4: BUTTON_4_SINGLE}),
        MapConv("action", mi="6.e.2.p.1", map={1: BUTTON_1_DOUBLE, 2: BUTTON_2_DOUBLE, 3: BUTTON_3_DOUBLE, 4: BUTTON_4_DOUBLE}),
        MapConv("action", mi="6.e.3.p.1", map={1: BUTTON_1_HOLD, 2: BUTTON_2_HOLD, 3: BUTTON_3_HOLD, 4: BUTTON_4_HOLD}),
        # --- 以下為騙過 UI 用的定義，不對應實體 mi 地址，僅供 UI 掃描 ---
        ConstConv("action", value="button_3_single"),
        ConstConv("action", value="button_3_double"),
        ConstConv("action", value="button_3_hold"),

        # --- 指示燈控制 ---
        BaseConv("led", "switch", mi="8.p.1"),
        
        # --- LED 亮度調整 (標記為設定實體) ---
        MathConv("brightness_white", "number", mi="10.p.3", min=0, max=100, entity=ENTITY_CONFIG),
        MathConv("brightness_orange", "number", mi="10.p.4", min=0, max=100, entity=ENTITY_CONFIG),
    ],
}, {
    # 科米其 牆壁開關 - KeMiQi M10 - 2 Key (PDID: 15080)
    # https://home.miot-spec.com/spec/kemiqi.switch.kmw13
    15080: ["科米其", "Double Wall Switch M10", "M10-2Key", "kemiqi.switch.kmw13"],
    "spec": [
        # --- 實體開關通道 ---
        BaseConv("switch_1", "switch", mi="2.p.1"),
        BaseConv("switch_2", "switch", mi="3.p.1"),
        
        # --- 模式選擇 (0: 有線+無線, 1: 純無線) ---
        MapConv("mode_1", "select", mi="2.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_2", "select", mi="3.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        
        # --- 按鍵動作 ---
        BaseConv("action", "sensor"),
        # 按鈕 1 (SIID 4)
        ConstConv("action", mi="4.e.1", value=BUTTON_1_SINGLE),
        ConstConv("action", mi="4.e.2", value=BUTTON_1_DOUBLE),
        ConstConv("action", mi="4.e.3", value=BUTTON_1_HOLD),
        # 按鈕 2 (SIID 5)
        ConstConv("action", mi="5.e.1", value=BUTTON_2_SINGLE),
        ConstConv("action", mi="5.e.2", value=BUTTON_2_DOUBLE),
        ConstConv("action", mi="5.e.3", value=BUTTON_2_HOLD),
        
        # --- 斷電記憶 ---
        # 0: On (通電開), 1: Off (通電關), 2: Restore (保持斷電前狀態)
        MapConv("default_status1", "select", mi="13.p.1", map={0: "On", 1: "Off", 2: "Restore"}),
        MapConv("default_status2", "select", mi="14.p.1", map={0: "On", 1: "Off", 2: "Restore"}),
        
    ],
}, {
    # 科米其 牆壁開關 - KeMiQi M10 - 3 Key (PDID: 15081)
    # https://home.miot-spec.com/spec/kemiqi.switch.kmw14
    15081: ["科米其", "Triple Wall Switch M10", "M10-3Key", "kemiqi.switch.kmw14"],
    "spec": [
        # --- 實體開關通道 (SIID 2, 3, 4) ---
        BaseConv("switch_1", "switch", mi="2.p.1"),
        BaseConv("switch_2", "switch", mi="3.p.1"),
        BaseConv("switch_3", "switch", mi="4.p.1"),
        
        # --- 模式選擇 (0: 有線+無線, 1: 純無線) ---
        MapConv("mode_1", "select", mi="2.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_2", "select", mi="3.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_3", "select", mi="4.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        
        # --- 按鍵動作感測器 (SIID 5, 6, 7) ---
        BaseConv("action", "sensor"),
        # 按鈕 1 (左)
        ConstConv("action", mi="5.e.1", value=BUTTON_1_SINGLE),
        ConstConv("action", mi="5.e.2", value=BUTTON_1_DOUBLE),
        ConstConv("action", mi="5.e.3", value=BUTTON_1_HOLD),
        # 按鈕 2 (中)
        ConstConv("action", mi="6.e.1", value=BUTTON_2_SINGLE),
        ConstConv("action", mi="6.e.2", value=BUTTON_2_DOUBLE),
        ConstConv("action", mi="6.e.3", value=BUTTON_2_HOLD),
        # 按鈕 3 (右) 
        ConstConv("action", mi="7.e.1", value=BUTTON_3_SINGLE),
        ConstConv("action", mi="7.e.2", value=BUTTON_3_DOUBLE),
        ConstConv("action", mi="7.e.3", value=BUTTON_3_HOLD),
        
        # --- 斷電記憶 ---
        # 0: On (通電開), 1: Off (通電關), 2: Restore (保持斷電前狀態)
        MapConv("default_status1", "select", mi="17.p.1", map={0: "On", 1: "Off", 2: "Restore"}),
        MapConv("default_status2", "select", mi="18.p.1", map={0: "On", 1: "Off", 2: "Restore"}),
        MapConv("default_status3", "select", mi="19.p.1", map={0: "On", 1: "Off", 2: "Restore"}),
        
    ],
}, {
    27151: ["Linptech", "Human Presence Sensor ES5(Side Mounted)", "linp.sensor_occupy.es5b"],
    "spec": [
        BoolConv("occupancy", "binary_sensor", mi="2.p.1078"),
        BaseConv("illuminance", "sensor", mi="2.p.1005"),
        BaseConv("has_someone_duration", "sensor", mi="2.p.1081", entity={"units": UNIT_MINUTES, "icon": "mdi:timer"}),
        MathConv("no_one_duration", "sensor", mi="2.p.1082", min=1, max=120, entity={"units": UNIT_MINUTES, "icon": "mdi:timer-off"}),
        MapConv("no_one_duration", mi="2.p.1078", map={1: 0}),
        MapConv("has_someone_duration", mi="2.p.1078", map={0: 0}),
        BoolConv("customized-property-2", "binary_sensor", mi="5.p.1019"),
        MapConv("no_one_duration", mi="5.p.1019", map={1: 0}),
        MapConv("has_someone_duration", mi="5.p.1019", map={0: 0}),
    ],    
}] + DEVICES