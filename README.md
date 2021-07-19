# vscode-snippet-pwn-template
将pwn模板写入到vscode的snippet文件中的小脚本
应该可以扩展成任意snippet生成，但是懒（


## 配置文件settings.json

示例如下
```json
{
    "jsonPath": "/Users/lemon/Library/Application Support/Code/User/snippets/python.json",
    "filePath": [
        "snippet/pwn.py",
        "snippet/menu.py",
        "snippet/format.py"
    ],
    "snippetName": [
        "pwn", 
        "menu",
        "64format"
    ]
}
```

其中jsonPath填入vscode中的json配置路径
snippet目录中放入想要生成的模板
filePath填入模板相对路径
snippetName填入snippet生成后的prefix名字
snippetName和filePath要对应起来

然后运行python3 run.py即可
