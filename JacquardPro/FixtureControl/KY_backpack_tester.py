# -*- coding=utf-8 -*-

from FixtureControl.KMY_tester_base import *


# 背包成品和半成品测试测试
class KMY_backpack_tester(KMY_tester_base):

    def __init__(self, config, limit_config):
        super(KMY_backpack_tester, self).__init__(config, limit_config)

    # 设备回原点
    def backhome(self):
        # 加速度无杆气缸电磁阀上
        status, msg = self._test_finished_step1()
        # 下压home
        if status:
            status = self.moon_motor.SetMoonsHome(self.config_obj.Push_down_slave)

        # roll home
        if status:
            if self.moon_motor.CheckHomeStatus(self.config_obj.Push_down_slave):
                self.moon_motor.SetMoonsHome(self.config_obj.Roll_slave)

        # 张紧气缸复位
        if status:
            status, msg = self.__test_finished_step3()

        # 夹紧气缸复位
        if status:
            status, msg = self.__test_finished_step4()

        # 等待结束在继续
        self._wait_moo_stop([self.config_obj.Push_down_slave, self.config_obj.Roll_slave])
        try:
            # 信号等复位
            if status:
                self.kmlio.set_start_lamp(0)
                self.kmlio.set_reset_lamp(1)
                self.kmlio.set_red(0)
                self.kmlio.set_green(0)
                self._buzzer()
            else:
                self.kmlio.set_red(0)
                self._buzzer(5)

            return status
        except Exception, ex:
            self._on_display_msg('reset', 'exception:{0}'.format(str(ex)), False)

    # 复位
    def reset(self):
        # 加速度无杆气缸电磁阀上
        status, msg = self._test_finished_step1()
        # 下压电机复位
        if status:
            status = self._Moveline(self.config_obj.Push_down_slave, 0, SPEED)
            self._on_display_msg('reset', 'down press motor reset {0}'.format('OK' if status else 'fail'), status)

        # 滚动电机复位
        if status:
            if self.moon_motor.CheckHomeStatus(self.config_obj.Push_down_slave):
                status = self._Moveline(self.config_obj.Roll_slave, 0, SPEED)
                self._on_display_msg('reset', 'roll motor reset {0}'.format('OK' if status else 'fail'), status)

        # 张紧气缸复位
        if status:
            status, msg = self.__test_finished_step3()

        # 夹紧气缸复位
        if status:
            status, msg = self.__test_finished_step4()

        # 等待结束在继续
        self._wait_moo_stop([self.config_obj.Push_down_slave, self.config_obj.Roll_slave])
        try:
            # 信号等复位
            if status:
                self.kmlio.set_start_lamp(0)
                self.kmlio.set_reset_lamp(1)
                self.kmlio.set_red(0)
                self.kmlio.set_green(0)
                self._buzzer()
            else:
                self.kmlio.set_red(0)
                self._buzzer(5)

            return status
        except Exception, ex:
            self._on_display_msg('reset', 'exception:{0}'.format(str(ex)), False)

    # 测试初始化
    def _test_init(self):
        try:
            self.current_item = 'test_init'
            self._on_item_start(self.current_item)
            # 夹紧
            msg = '_test_init ok'
            test_status = self._stretch_relax()
            # 4. 张紧
            if test_status:
                test_status = self._stretch_tensioning()
                if test_status is False:
                    msg = '_stretch_tensioning fail'
            else:
                msg = '_stretch_relax fail'
            return test_status
        except Exception, ex:
            test_status = False
            msg = 'exception:' + ex.message
            return test_status
        finally:
            self._on_item_end(self.current_item, test_status, msg, msg)
            self._on_display_msg('_test_init', msg, test_status)

    # 滚动测试
    def _roll_test(self, dut=True):
        # 加速度无杆气缸电磁阀上状态检测
        test_status, msg = self._check_accelerated_up()

        # 1. 运动到下压起始位置(测试位置)
        if test_status:
            test_status = self.__roll_test_step1()

        # 2.下压电机运动以及找到接触点
        if test_status:
            test_status = self.__roll_test_step2()

        # 空跑，不同dut通讯采集数据
        if dut is False:
            slave = self.config_obj.Roll_slave
            pos = self.config_obj.Roll_pos
            test_status = self._Moveline(slave, pos, ROLL_SPEED)
            return test_status

        # 3开启t命令
        if test_status:
            test_status = self._open_diff()

        # # 4.开始滚动
        # if test_status:
        #     test_status = self.__roll_test_step3()

        # 5.开始采集difference数据---这个函数需要修改
        if test_status:
            test_status = self._roll_check_difference()

        return test_status

    # 采集并验证difference数据---已修改，还未验证---liyunhe
    def _roll_check_difference(self):
        try:
            self.current_item = 'check_difference_step'
            self._on_item_start(self.current_item)
            test_status = True
            slave = self.config_obj.Roll_slave
            pos = self.config_obj.Roll_pos
            # 开始采集dut difference数据
            self.mcu.mcu_com.Start_T_Collect()
            test_status = self._Moveline(slave, pos, ROLL_SPEED, False)
            raed_str = ''
            while True:
                raed_str += self.mcu.mcu_com.Read_Buff()
                if self.moon_motor.StopStatus(slave):
                    rdstr = self.mcu.mcu_com.Read_Buff()
                    if len(rdstr) == 0:
                        time.sleep(0.01)
                        continue
                    raed_str += rdstr
                    self._on_touch_diffenrence(rdstr)
                    # self.mcu.mcu_com.close_up()
                    self.mcu.mcu_com.ClosePort()
                    break

            try:
                file_path = self.get_save_dir() + "\\" + 'roll_t.txt'
                with open(file_path, 'w') as fp:
                    fp.write(raed_str)
            except Exception,ex:
                pass

            self.mcu.t_cmdInfo.to_touch_diff(raed_str)

            # 等待电机运动结束
            # self._wait_moo_stop([self.config_obj.Roll_slave])
            # self._stop_collect_diff()
            # time.sleep(2)
            #  进行数据处理
            file_path = self.get_save_dir() + "\\" + self.current_sn + \
                        "differnece_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".csv"

            # test_status, msg = self.mcu.difference_data_processing(file_path)
            test_status,msg = self.mcu.difference_data_processing(file_path)

            # 数据判定
            # 1. Max Touch Capacitance判定
            status1 = self._max_touch_cap()
            # 2. Touch Saturation 判定
            status2 = self._touch_Saturations()
            # 3. 触摸位置判定
            status3 = True
            # status3 = self._touch_pos()
            test_status = status1 and status2 and status3
            if test_status:
                msg = "check difference step ok"
            else:
                msg += ",check difference step fail"
            return test_status
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status
        finally:
            self.current_item = 'check_difference_step'
            self._on_item_end(self.current_item, test_status, str(test_status), msg)
            self._on_display_msg('_roll_check_difference', msg, test_status)

    # 运动到下压起始位置(测试位置)
    def __roll_test_step1(self):
        try:
            self.current_item = 'roll_move_test_position'
            self._on_item_start(self.current_item)
            msg = '__roll_test_step1 ok'
            slave = self.config_obj.Roll_slave
            pos = self.config_obj.Roll_start_pos
            # 开始运动到指定位置
            test_status = self._Moveline(slave, pos, SPEED)
            if test_status is False:
                msg = 'move roll test pos fail'

            return test_status
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status
        finally:
            self._on_item_end(self.current_item, test_status, str(test_status), msg)
            self._on_display_msg('__roll_test_step1', msg, test_status)

    # 滚动测试->下压电机运动
    def __roll_test_step2(self):
        try:
            self.current_item = 'roll_test_step2'
            self._on_item_start(self.current_item)
            msg = '__roll_test_step2 ok'
            slave = self.config_obj.Push_down_slave
            pos1 = self.config_obj.Pressure_target_pos
            pos = self.config_obj.Roll_pressure_pos
            maxN = self.config_obj.MaxN
            # 检测之前清除loadcell压力表数据
            self._clear_loadcell()
            # 运动到目标1pos
            test_status = self._press_to_pos(self.loadcell, slave, pos1, SPEED)
            if test_status is False:
                msg = 'roll_test_step2 run target pos1 fail'

            # 开始运动并检测压力范围
            if test_status:
                # 检测之前清除loadcell压力表数据
                # self._clear_loadcell()
                test_status = self._run_to_InitN(self.loadcell, slave, pos, 50, maxN)
                time.sleep(1)      # 等待压力表稳定
                if test_status is False:
                    msg = 'roll_test_step2 touch fail'

            return test_status
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status
        finally:
            self._on_item_end(self.current_item, test_status, str(test_status), msg)
            self._on_display_msg('__roll_test_step2', msg, test_status)

    # 滚动测试->开启滚动模式
    def __roll_test_step3(self):
        try:
            self.current_item = 'roll_test_step3'
            self._on_item_start(self.current_item)
            msg = '__roll_test_step3 fail'
            # 滚动电机运动
            slave = self.config_obj.Roll_slave
            pos = self.config_obj.Roll_pos
            # 可以测试产品时，必须使用 test_status = self._Moveline(slave, pos, ROLL_SPEED, False)
            test_status = self._Moveline(slave, pos, ROLL_SPEED, False)
            if test_status:
                msg = 'roll motor move ok '
            else:
                msg = 'roll motor move fail '
            return test_status
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status
        finally:
            self.current_item = 'roll_test_step3'
            self._on_item_end(self.current_item, test_status, str(test_status), msg)
            self._on_display_msg('__roll_test_step3', msg, test_status)

    # 滚动测试->复位滚动测试动作
    def __roll_test_step4(self):
        try:
            self.current_item = 'roll_test_step4'
            self._on_item_start(self.current_item)
            msg = '__roll_test_step4 fail'
            # 下压电机复位
            test_status = self._Moveline(self.config_obj.Push_down_slave, 0, SPEED)
            msg = 'press moon slave={0} reset {1}'.format(self.config_obj.Push_down_slave,
                                                          'ok' if test_status else 'fail')

            return test_status
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status
        finally:
            self._on_item_end(self.current_item, test_status, str(test_status), msg)
            self._on_display_msg('__roll_test_step4', msg, test_status)

    # 振动测试
    def _vibration_test(self):
        # 1.运动到振动器位置
        test_status = self.__vibration_move_step1()
        # 2.加速度无杆气缸电磁阀下
        if test_status:
            test_status = self.__vibration_test_step2()
        # 3.启动振动并采集数据
        if test_status:
            time.sleep(1)
            test_status = self._vibration_check()

        return test_status

    # 运动到振动测试位置
    def __vibration_move_step1(self):
        try:
            self.current_item = 'vibration_move_step1'
            self._on_item_start(self.current_item)
            test_status = False
            msg = '__vibration_move_step1 fail'

            # 下压电机复位
            p_slav = self.config_obj.Push_down_slave
            test_status = self._Moveline(p_slav, 0, SPEED, True)
            # 移动电机移动到振动器位置
            if test_status:
                r_slave = self.config_obj.Roll_slave
                if self.moon_motor.CheckHomeStatus(self.config_obj.Push_down_slave):
                    test_status = self._Moveline(r_slave, self.config_obj.Vibrator_pos, SPEED)
                    if test_status is False:
                        msg = "Push_down motor not in home"
                else:
                    msg = "roll motor not in position, slave={0}".format(r_slave)
            else:
                msg = "press motor not in position, slave={0}".format(p_slav)
            return test_status
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ ex.message
            return test_status
        finally:
            self._on_item_end(self.current_item, test_status, str(test_status), msg)
            self._on_display_msg('__vibration_move_step1', msg, test_status)

    # 振动测试->加速度无杆气缸电磁阀下
    def __vibration_test_step2(self):
        try:
            self.current_item = 'vibration_test_step2'
            self._on_item_start(self.current_item)
            msg = '__vibration_test_step2 ok'
            test_status = True
            status, set_data = self.kmlio.set_accelerated_down(False)
            if status is True:
                value, data = self.kmlio.get_accelerated_down(0, True)
                if value != 1:
                    test_status = False
                    msg = 'get_accelerated_down fail'
                else:
                    time.sleep(1)        # 等待稳定
            else:
                test_status = False
                msg = 'set_accelerated_down fail'
            return test_status
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status
        finally:
            self._on_item_end(self.current_item, test_status, str(test_status), msg)
            self._on_display_msg('__vibration_test_step2', msg, test_status)

    # 测试结束，正常复位
    def _test_finished(self):
        self.current_item = 'test_finished'
        self._on_item_start(self.current_item)
        # 加速度无杆气缸电磁阀上
        test_status, msg = self._test_finished_step1()
        # 滚动电机复位
        if test_status:
            if self.moon_motor.CheckHomeStatus(self.config_obj.Push_down_slave):
                test_status, msg = self.__test_finished_step2()
        # 张紧气缸释放
        if test_status:
            test_status, msg = self.__test_finished_step3()
        # 夹爪气缸释放
        if test_status:
            test_status, msg = self.__test_finished_step4()

        try:
            # 信号等复位
            if test_status:
                self.kmlio.set_start_lamp(0)
                self.kmlio.set_reset_lamp(1)
                self.kmlio.set_red(0)
                self.kmlio.set_green(0)
                self._buzzer(2)
            else:
                self.kmlio.set_red(0)
                self._buzzer(5)
        except Exception, ex:
            msg = 'io control exception:' + ex.message
            self._on_display_msg('_test_finished', msg, False)

        self._on_item_end(self.current_item, test_status, str(test_status), msg)
        return test_status

    # 滚动电机复位
    def __test_finished_step2(self):
        try:
            msg = '__test_finished_step2 ok'
            test_status = self._Moveline(self.config_obj.Roll_slave, 0, SPEED)
            msg = 'roll moon reset,slave={0} {1}'.format(self.config_obj.Roll_slave, 'ok' if test_status else 'fail')
            return test_status, msg
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status, msg
        finally:
            self._on_display_msg('__test_finished_step2', msg, test_status)

    # 张紧气缸释放
    def __test_finished_step3(self):
        try:
            test_status = True
            msg = '__test_finished_step3 ok'
            status, set_data = self.kmlio.set_stretch_tensioning(1)
            if status is True:
                value, data = self.kmlio.get_stretch_relax(1, True)  # 张紧气缸放松
                if value != 1:
                    test_status = False
                    msg = 'get_stretch_relax  fail value={0}, data={1}'.format(value, data)
            else:
                test_status = False
                msg = 'set_stretch_tensioning fail'

            return test_status, msg
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status, msg
        finally:
            self._on_display_msg('__test_finished_step3', msg, test_status)

    # 夹爪气缸释放
    def __test_finished_step4(self):
        try:
            test_status = True
            msg = '__test_finished_step4 ok'
            status, set_data = self.kmlio.set_stretch_relax(1)
            if status is True:
                value, data = self.kmlio.get_claw_loosen(0, True)
                if value != 1:
                    test_status = False
                    msg = 'get_claw_loosen  fail, value={0}, data={1}'.format(value, data)
            else:
                test_status = False
                msg = 'set_stretch_relax 0 fail'

            return test_status, msg
        except Exception, ex:
            test_status = False
            msg = 'exception:'+ex.message
            return test_status, msg
        finally:
            self._on_display_msg('__test_finished_step4', msg, test_status)


if __name__ == "__main__":
    appconfig = APPConfigparse.APPConfigparse(r'../config.ini')
    obj = KMY_backpack_tester(appconfig)

    # st = '\xbe\xdc\xbe\xf8\xb7\xc3\xce\xca\xa1\xa3'
    # b = repr(st)
    # print unicode(eval(b), "gbk")

    init_st = obj.check_connect(auto=True, port_list=["COM10"])
    for i in range(0, len(init_st)):
        print init_st[i]
    while True:
        acc_info = obj.haptics_probe.read_data()
        print '-'.center(100, '-')
        print 'temperature={0}'.format(acc_info.temperature)
        print 'accelerated speed ={0},{1},{2}'.format(acc_info.xyz_acc[0], acc_info.xyz_acc[1], acc_info.xyz_acc[2])
        print 'angular speed ={0},{1},{2}'.format(acc_info.xyz_angle_acc[0], acc_info.xyz_angle_acc[1],
                                                  acc_info.xyz_angle_acc[2])
        print 'angle = {0},{1},{2}'.format(acc_info.xyx_angle[0], acc_info.xyx_angle[1], acc_info.xyx_angle[2])
        print '-'.center(100, '-')
        time.sleep(0.02)