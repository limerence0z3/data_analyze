from db import (
    getGrowthRateOfAgeMarriage, getGrowthRateOfUnMarriage, getGrowthRateOfCPI,
    getGrowthRateOfFertility, getCorrelationWithFertility
)

import math

if __name__ == '__main__':
    print(abs(getCorrelationWithFertility(getGrowthRateOfAgeMarriage())))
    print(abs(getCorrelationWithFertility(getGrowthRateOfUnMarriage())))
    print(abs(getCorrelationWithFertility(getGrowthRateOfCPI())))
