# coding:utf-8
from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'RL', u'TL'])
@Js
def PyJsHoisted_RL_(a, b, this, arguments, var=var):
    var = Scope({u'a':a, u'this':this, u'b':b, u'arguments':arguments}, var)
    var.registers([u'a', u'c', u'b', u'd', u'Yb', u't'])
    var.put(u't', Js(u'a'))
    var.put(u'Yb', Js(u'+'))
    #for JS loop
    var.put(u'c', Js(0.0))
    while (var.get(u'c')<(var.get(u'b').get(u'length')-Js(2.0))):
        try:
            var.put(u'd', var.get(u'b').callprop(u'charAt', (var.get(u'c')+Js(2.0))))
            var.put(u'd', ((var.get(u'd').callprop(u'charCodeAt', Js(0.0))-Js(87.0)) if (var.get(u'd')>=var.get(u't')) else var.get(u'Number')(var.get(u'd'))))
            var.put(u'd', (PyJsBshift(var.get(u'a'),var.get(u'd')) if (var.get(u'b').callprop(u'charAt', (var.get(u'c')+Js(1.0)))==var.get(u'Yb')) else (var.get(u'a')<<var.get(u'd'))))
            var.put(u'a', (((var.get(u'a')+var.get(u'd'))&Js(4294967295.0)) if (var.get(u'b').callprop(u'charAt', var.get(u'c'))==var.get(u'Yb')) else (var.get(u'a')^var.get(u'd'))))
        finally:
                var.put(u'c', Js(3.0), u'+')
    return var.get(u'a')
PyJsHoisted_RL_.func_name = u'RL'
var.put(u'RL', PyJsHoisted_RL_)
@Js
def PyJsHoisted_TL_(a, this, arguments, var=var):
    var = Scope({u'a':a, u'this':this, u'arguments':arguments}, var)
    var.registers([u'a', u'b', u'e', u'g', u'f', u'm', u'k', u'$b', u'Zb', u'b1', u'jd'])
    var.put(u'k', Js(u''))
    var.put(u'b', Js(406644.0))
    var.put(u'b1', Js(3293161072.0))
    var.put(u'jd', Js(u'.'))
    var.put(u'$b', Js(u'+-a^+6'))
    var.put(u'Zb', Js(u'+-3^+b+-f'))
    #for JS loop
    var.put(u'e', Js([]))
    var.put(u'f', Js(0.0))
    var.put(u'g', Js(0.0))
    while (var.get(u'g')<var.get(u'a').get(u'length')):
        try:
            var.put(u'm', var.get(u'a').callprop(u'charCodeAt', var.get(u'g')))
            def PyJs_LONG_2_(var=var):
                def PyJs_LONG_1_(var=var):
                    def PyJs_LONG_0_(var=var):
                        return PyJsComma(PyJsComma(var.put(u'm', ((Js(65536.0)+((var.get(u'm')&Js(1023.0))<<Js(10.0)))+(var.get(u'a').callprop(u'charCodeAt', var.put(u'g',Js(var.get(u'g').to_number())+Js(1)))&Js(1023.0)))),var.get(u'e').put((var.put(u'f',Js(var.get(u'f').to_number())+Js(1))-Js(1)), ((var.get(u'm')>>Js(18.0))|Js(240.0)))),var.get(u'e').put((var.put(u'f',Js(var.get(u'f').to_number())+Js(1))-Js(1)), (((var.get(u'm')>>Js(12.0))&Js(63.0))|Js(128.0))))
                    return PyJsComma((PyJs_LONG_0_() if (((Js(55296.0)==(var.get(u'm')&Js(64512.0))) and ((var.get(u'g')+Js(1.0))<var.get(u'a').get(u'length'))) and (Js(56320.0)==(var.get(u'a').callprop(u'charCodeAt', (var.get(u'g')+Js(1.0)))&Js(64512.0)))) else var.get(u'e').put((var.put(u'f',Js(var.get(u'f').to_number())+Js(1))-Js(1)), ((var.get(u'm')>>Js(12.0))|Js(224.0)))),var.get(u'e').put((var.put(u'f',Js(var.get(u'f').to_number())+Js(1))-Js(1)), (((var.get(u'm')>>Js(6.0))&Js(63.0))|Js(128.0))))
                return (var.get(u'e').put((var.put(u'f',Js(var.get(u'f').to_number())+Js(1))-Js(1)), var.get(u'm')) if (Js(128.0)>var.get(u'm')) else PyJsComma((var.get(u'e').put((var.put(u'f',Js(var.get(u'f').to_number())+Js(1))-Js(1)), ((var.get(u'm')>>Js(6.0))|Js(192.0))) if (Js(2048.0)>var.get(u'm')) else PyJs_LONG_1_()),var.get(u'e').put((var.put(u'f',Js(var.get(u'f').to_number())+Js(1))-Js(1)), ((var.get(u'm')&Js(63.0))|Js(128.0)))))
            PyJs_LONG_2_()
        finally:
                (var.put(u'g',Js(var.get(u'g').to_number())+Js(1))-Js(1))
    var.put(u'a', var.get(u'b'))
    #for JS loop
    var.put(u'f', Js(0.0))
    while (var.get(u'f')<var.get(u'e').get(u'length')):
        try:
            PyJsComma(var.put(u'a', var.get(u'e').get(var.get(u'f')), u'+'),var.put(u'a', var.get(u'RL')(var.get(u'a'), var.get(u'$b'))))
        finally:
                (var.put(u'f',Js(var.get(u'f').to_number())+Js(1))-Js(1))
    var.put(u'a', var.get(u'RL')(var.get(u'a'), var.get(u'Zb')))
    var.put(u'a', (var.get(u'b1') or Js(0.0)), u'^')
    ((Js(0.0)>var.get(u'a')) and var.put(u'a', ((var.get(u'a')&Js(2147483647.0))+Js(2147483648.0))))
    var.put(u'a', Js(1000000.0), u'%')
    return ((var.get(u'a').callprop(u'toString')+var.get(u'jd'))+(var.get(u'a')^var.get(u'b')))
PyJsHoisted_TL_.func_name = u'TL'
var.put(u'TL', PyJsHoisted_TL_)


print(PyJsHoisted_TL_("xxxxx"))