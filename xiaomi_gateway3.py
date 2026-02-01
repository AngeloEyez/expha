# /config/xiaomi_gateway3.py
from custom_components.xiaomi_gateway3.core.devices import *

DEVICES = [{
    # 4-key 牆壁開關配置 - Linptech T1 系列
    26373: ["Linptech", "T2 4-Key Switch", "linp.switch.t2dbw4"],
    "spec": [
        # --- 四路開關 (Property) ---
        # 鍵名必須為 switch_1~4，這會直接對應到診斷報告的 params 中
        BaseConv("switch_1", "switch", mi="2.p.1"),
        BaseConv("switch_2", "switch", mi="3.p.1"),
        BaseConv("switch_3", "switch", mi="4.p.1"),
        BaseConv("switch_4", "switch", mi="5.p.1"),

        # --- 模式設定 (Property) ---
        # 0: 有線與無線 (轉無線開關模式), 1: 純無線
        MapConv("mode_1", "select", mi="2.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_2", "select", mi="3.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_3", "select", mi="4.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_4", "select", mi="5.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),

        # --- 按鍵動作 (Event) ---
        # 根據 Log: siid 6, eiid 1。MapConv 會自動解析 arguments 中的第一個值
        BaseConv("action", "sensor"),
        MapConv("action", mi="6.e.1", map={
            1: "button_1_single",
            2: "button_2_single",
            3: "button_3_single",
            4: "button_4_single"
        }),

        # --- 硬體控制 ---
        BaseConv("led", "switch", mi="8.p.1"),
        # 移除未定義的 ENTITY_CONFIG 常量以確保載入成功
        #MathConv("brightness_white", "number", mi="10.p.3", min=0, max=100),
        #MathConv("brightness_orange", "number", mi="10.p.4", min=0, max=100),
    ],
    # 科米其 牆壁開關 - KeMiQi M10 - 2 Key
    15080: ["科米其", "Double Wall Switch M10", "M10-2Key"],
    "spec": [
        BaseConv("switch_1", "switch", mi="2.p.1"),
        BaseConv("switch_2", "switch", mi="3.p.1"),
        MapConv("mode_1", "select", mi="2.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_2", "select", mi="3.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        BaseConv("action", "sensor"),
        ConstConv("action", mi="5.e.1", value=BUTTON_1_SINGLE),
        ConstConv("action", mi="5.e.2", value=BUTTON_1_DOUBLE),
        ConstConv("action", mi="5.e.3", value=BUTTON_1_HOLD),
        ConstConv("action", mi="6.e.1", value=BUTTON_2_SINGLE),
        ConstConv("action", mi="6.e.2", value=BUTTON_2_DOUBLE),
        ConstConv("action", mi="6.e.3", value=BUTTON_2_HOLD),
        BaseConv("led", "switch", mi="8.p.1"),
        MathConv("brightness_white", "number", mi="10.p.3", min=0, max=100, entity=ENTITY_CONFIG),
        MathConv("brightness_orange", "number", mi="10.p.4", min=0, max=100, entity=ENTITY_CONFIG),
    ],
}, {
    # 科米其 牆壁開關 - KeMiQi M10 - 3 Key
    15081: ["科米其", "Triple Wall Switch M10", "M10-3Key"],
    "spec": [
        BaseConv("switch_1", "switch", mi="2.p.1"),
        BaseConv("switch_2", "switch", mi="3.p.1"),
        BaseConv("switch_3", "switch", mi="4.p.1"),
        MapConv("mode_1", "select", mi="2.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_2", "select", mi="3.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_3", "select", mi="4.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        BaseConv("action", "sensor"),
        ConstConv("action", mi="5.e.1", value=BUTTON_1_SINGLE),
        ConstConv("action", mi="5.e.2", value=BUTTON_1_DOUBLE),
        ConstConv("action", mi="5.e.3", value=BUTTON_1_HOLD),
        ConstConv("action", mi="6.e.1", value=BUTTON_2_SINGLE),
        ConstConv("action", mi="6.e.2", value=BUTTON_2_DOUBLE),
        ConstConv("action", mi="6.e.3", value=BUTTON_2_HOLD),
        ConstConv("action", mi="7.e.1", value=BUTTON_3_SINGLE),
        ConstConv("action", mi="7.e.2", value=BUTTON_3_DOUBLE),
        ConstConv("action", mi="7.e.3", value=BUTTON_3_HOLD),
        BaseConv("led", "switch", mi="8.p.1"),
        MathConv("brightness_white", "number", mi="10.p.3", min=0, max=100, entity=ENTITY_CONFIG),
        MathConv("brightness_orange", "number", mi="10.p.4", min=0, max=100, entity=ENTITY_CONFIG),
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