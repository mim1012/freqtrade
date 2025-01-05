from freqtrade.strategy import IStrategy, DecimalParameter, IntParameter
from pandas import DataFrame
import talib.abstract as ta
import pandas_ta as pta
import numpy as np

class UpbitStrategy(IStrategy):
    """
    업비트용 기본 전략
    RSI + 볼린저밴드 조합
    """
    INTERFACE_VERSION = 3

    # 최소 ROI 설정
    minimal_roi = {
        "0": 0.05,    # 5% 이상 수익시 즉시 매도
        "30": 0.025,  # 30분 후 2.5% 이상시 매도
        "60": 0.015,  # 60분 후 1.5% 이상시 매도
        "120": 0.01   # 120분 후 1% 이상시 매도
    }

    # 손절 설정
    stoploss = -0.05  # 5% 손실시 손절

    # 트레일링 스탑
    trailing_stop = True
    trailing_stop_positive = 0.01
    trailing_stop_positive_offset = 0.02
    trailing_only_offset_is_reached = True

    # 기본 설정
    timeframe = '5m'
    process_only_new_candles = True
    use_exit_signal = True
    exit_profit_only = False
    ignore_roi_if_entry_signal = False

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        
        # 볼린저 밴드
        bollinger = pta.bbands(dataframe['close'], length=20, std=2)
        dataframe['bb_upperband'] = bollinger['BBU_20_2.0']
        dataframe['bb_middleband'] = bollinger['BBM_20_2.0']
        dataframe['bb_lowerband'] = bollinger['BBL_20_2.0']
        
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['rsi'] < 30) &  # RSI 과매도
                (dataframe['close'] < dataframe['bb_lowerband'])  # 볼린저 밴드 하단 돌파
            ),
            'enter_long'] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['rsi'] > 70) |  # RSI 과매수
                (dataframe['close'] > dataframe['bb_upperband'])  # 볼린저 밴드 상단 돌파
            ),
            'exit_long'] = 1
        return dataframe 