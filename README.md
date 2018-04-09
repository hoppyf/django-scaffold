### django api 脚手架

- 集成三方drf、token认证
- 配置drf参数
- 提供开发+线上配置文件，通过设定环境变量env
- 提供异常处理handler，标准化response返回格式
- 提供开发环境下的serializer异常提示
- 抽象Model和ModelSerializer
- 提供api demo，参见product app
- 提供自定义user类，可在此基础上扩展

```
response格式
{
    "code": 0,
    "msg": "",
    "data": ""
}
```
