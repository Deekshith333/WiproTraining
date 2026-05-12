from behave import given, when, then

from utils.logger import LogGen

logger =

@given(u'User launches Demoblaze application')
def step_impl(context):


@when(u'User clicks on Sign up menu')
def step_impl(context):


@when(u'User enters signup username "useraaaaa"')
def step_impl(context):



@when(u'User enters signup password "pwdaaaaa"')
def step_impl(context):