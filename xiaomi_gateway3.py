# /config/xiaomi_gateway3.py
from custom_components.xiaomi_gateway3.core.devices import *

DEVICES = [{
    # 4-key 牆壁開關配置 - Linptech T1 系列
    26373: ["Linptech", "Quadruple Wall Switch T1", "linp.switch.t2dbw4"],
    "spec": [
        # 四個開關通道
        BaseConv("switch_1", "switch", mi="2.p.1"),
        BaseConv("switch_2", "switch", mi="3.p.1"),
        BaseConv("switch_3", "switch", mi="4.p.1"),
        BaseConv("switch_4", "switch", mi="5.p.1"),
        # 四個模式選擇（有線+無線 或 純無線）
        MapConv("mode_1", "select", mi="2.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_2", "select", mi="3.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_3", "select", mi="4.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        MapConv("mode_4", "select", mi="5.p.2", map={0: "Wired And Wireless", 1: "Wireless"}),
        # 動作感測器
        BaseConv("action", "sensor"),
        # 按鈕 1 的三種動作（單擊、雙擊、長按）
        ConstConv("action", mi="5.e.1", value=BUTTON_1_SINGLE),
        ConstConv("action", mi="5.e.2", value=BUTTON_1_DOUBLE),
        ConstConv("action", mi="5.e.3", value=BUTTON_1_HOLD),
        # 按鈕 2 的三種動作
        ConstConv("action", mi="6.e.1", value=BUTTON_2_SINGLE),
        ConstConv("action", mi="6.e.2", value=BUTTON_2_DOUBLE),
        ConstConv("action", mi="6.e.3", value=BUTTON_2_HOLD),
        # 按鈕 3 的三種動作
        ConstConv("action", mi="7.e.1", value=BUTTON_3_SINGLE),
        ConstConv("action", mi="7.e.2", value=BUTTON_3_DOUBLE),
        ConstConv("action", mi="7.e.3", value=BUTTON_3_HOLD),
        # 按鈕 4 的三種動作
        ConstConv("action", mi="8.e.1", value=BUTTON_4_SINGLE),
        ConstConv("action", mi="8.e.2", value=BUTTON_4_DOUBLE),
        ConstConv("action", mi="8.e.3", value=BUTTON_4_HOLD),
        # LED 控制
        BaseConv("led", "switch", mi="8.p.1"),
        # 白光亮度調整
        MathConv("brightness_white", "number", mi="10.p.3", min=0, max=100, entity=ENTITY_CONFIG),
        # 橙光亮度調整
        MathConv("brightness_orange", "number", mi="10.p.4", min=0, max=100, entity=ENTITY_CONFIG),
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