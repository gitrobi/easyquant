
from easyquant import StrategyTemplate
from easyquant import DefaultLogHandler


class Strategy(StrategyTemplate):
    name = '测试策略2'

    def strategy(self, event):
        self.log.info('策略2触发')
        self.log.info('行情数据: 华宝油气 %s' % event.data['162411'])
        self.log.info('检查持仓 %s' % self.user.position)
        #self.log.info('\n')

    def log_handler(self):
        """自定义 log 记录方式"""
        return DefaultLogHandler(self.name, log_type='stdout', filepath='logs/demo2.log')
