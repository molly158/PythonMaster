#闭包的核心：不仅能执行代码 还能“记住”创建时的环境和配置

def outer(logo):
    def inner(msg):
        print(f"<logo>{msg}<logo>")
    return inner
fn=outer("SCEF Formation")
fn("Hello")
fn("World")

fn1=outer("Phone")
fn1("Huawei")
fn1("Apple")