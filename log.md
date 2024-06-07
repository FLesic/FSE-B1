第一次联调：

- 创建账户UI
- 数字输入限定只能输入数字（所有的）
- cashier_id传入问题（其他页面的更改）
- 定期存款暂定传入月份，前端标注单位，后端做出相应处理
- 是否续期设置默认值
- 前端更改输入的存款/取款/转账金额为float
- 累计存款account_id传入问题
- 补发操作补全
- 开设账户后端返回accountID
- 开设账户成功加交互
- 存款记录显示的问题（好多table）
- 自动续期后端判断有问题
- 定期存款默认值清除
- 累计存款后端balance计算错误
- 隐藏密码
- 转账记录查询有问题t

## 统一

URL

五个组统一使用登录模块
localhost:8000/user/login

localhost:8000/employee/login
（可选择登录的身份）

登录后：

localhost:8000/user/大组的功能模块/各个模块具体的页面显示

localhost:8000/employee/不同职员的名称/不同职员的操作

定期存款

活期存款：1000

待定存款：


现在指的都是活期
1月15日存入1500
2月1日



def balancechange(accountID, (float)delta):
