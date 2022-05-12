from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField,DateTimeField, Form,validators,widgets
from wtforms.validators import DataRequired, EqualTo, Length
from flask import Flask, render_template, request, redirect
from wtforms.fields import simple,html5


class registerForm(Form):
    card_id = simple.StringField(
        #label='学号：',
        validators=[
            validators.DataRequired(message='学号不能为空'),
            validators.Length(min=11, message='学号长度必须是%(min)d位！')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"输入学号"}
    )
    student_name = simple.StringField(
        # label='学生姓名：',
        validators=[
            validators.DataRequired(message='姓名不能为空'),
            validators.Length(min=2, max=4, message='姓名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',
                   "placeholder": "输入学生姓名"}
    )
    password = simple.PasswordField(
        #label='用户密码：',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(min=5, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="[0-9a-zA-Z]{5,}",message='密码不允许使用特殊字符')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"输入用户密码"}
    )
    RepeatPassword = simple.PasswordField(
        #label='重复密码：',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(min=5, message='密码长度必须大于%(min)d'),
            validators.Regexp(regex="[0-9a-zA-Z]{5,}",message='密码不允许使用特殊字符'),
            validators.EqualTo("password",message="两次密码输入必须一致,龟孙")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"再次输入密码"}
    )
    # enroll_time = DateTimeField("注册时间",format="%Y-%m-%d %H:%M:%S")
    # valid_time = DateTimeField("毕业时间",format="%Y-%m-%d %H:%M:%S")
    submit = simple.SubmitField(
        label="用 户 注 册",
        render_kw={ "class":"btn btn-success" }
    )


class Login(FlaskForm):
    account = StringField(u'账号', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登录')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'原密码', validators=[DataRequired()])
    password = PasswordField(u'新密码', validators=[DataRequired(), EqualTo('password2', message=u'两次密码必须一致！')])
    password2 = PasswordField(u'确认新密码', validators=[DataRequired()])
    submit = SubmitField(u'确认修改')


class EditInfoForm(FlaskForm):
    name = StringField(u'用户名', validators=[Length(1, 32)])
    submit = SubmitField(u'提交')


class SearchBookForm(FlaskForm):
    methods = [('book_name', '书名'), ('author', '作者'), ('class_name', '类别'), ('isbn', 'ISBN')]
    method = SelectField(choices=methods, validators=[DataRequired()], coerce=str)
    content = StringField(validators=[DataRequired()])
    submit = SubmitField('搜索')


class SearchStudentForm(FlaskForm):
    card = StringField(validators=[DataRequired()])
    submit = SubmitField('搜索')


class StoreForm(FlaskForm):
    barcode = StringField(validators=[DataRequired(), Length(6)])
    isbn = StringField(validators=[DataRequired(), Length(13)])
    location = StringField(validators=[DataRequired(), Length(1, 32)])
    submit = SubmitField(u'提交')


class NewStoreForm(FlaskForm):
    isbn = StringField(validators=[DataRequired(), Length(13)])
    book_name = StringField(validators=[DataRequired(), Length(1, 64)])
    press = StringField(validators=[DataRequired(), Length(1, 32)])
    author = StringField(validators=[DataRequired(), Length(1, 64)])
    class_name = StringField(validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField(u'提交')


class BorrowForm(FlaskForm):
    card = StringField(validators=[DataRequired()])
    book_name = StringField(validators=[DataRequired()])
    submit = SubmitField(u'搜索')
