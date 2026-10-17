#include <Adafruit_VL53L0X.h>
#include <vl53l0x_api.h>
#include <vl53l0x_api_calibration.h>
#include <vl53l0x_api_core.h>
#include <vl53l0x_api_ranging.h>
#include <vl53l0x_api_strings.h>
#include <vl53l0x_def.h>
#include <vl53l0x_device.h>
#include <vl53l0x_i2c_platform.h>
#include <vl53l0x_interrupt_threshold_settings.h>
#include <vl53l0x_platform.h>
#include <vl53l0x_platform_log.h>
#include <vl53l0x_tuning.h>
#include <vl53l0x_types.h>

#include <Adafruit_CircuitPlayground.h>
#include <Adafruit_Circuit_Playground.h>

#include <Wire.h>
#include <Adafruit_VL53L0X.h>

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup()
{
    Serial.begin(115200);
    if (!lox.begin())
    {
        Serial.println("Sensor bulunamadi");
        while (1)
            ;
    }
}

void loop()
{
    VL53L0X_RangingMeasurementData_t olcum;
    lox.rangingTest(&olcum, false);
    if (olcum.RangeStatus != 4)
    {
        Serial.println(olcum.RangeMilliMeter);
    }
    delay(50);
}
