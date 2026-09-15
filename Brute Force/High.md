# DVWA Brute Force High 暴力破解

## 环境信息
- 靶场：DVWA
- 漏洞模块：Brute Force（暴力破解）
- 安全等级：High
- 漏洞原理：增加了CSRF token（user_token），每次请求必须携带一次性token，防止批量自动请求；但**没有验证码，无账号锁定**，依然可以爆破，每次请求需要先获取新token。

## 源码分析
```php
<?php
if( isset( $_GET[ 'Login' ] ) ) {
    // 检查CSRF token
    checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ] );

    $user = $_GET[ 'username' ];
    $pass = $_GET[ 'password' ];

    $pass = md5( $pass );

    $query  = "SELECT * FROM users WHERE user = '$user' AND password = '$pass';";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

    if ($result && mysqli_num_rows($result) == 1 ) {
        echo "<p>Welcome to the password protected area admin</p>";
    } else {
        sleep(3);
        echo "<pre><br>Username and/or password incorrect.</pre>";
    }
}
generateSessionToken();
?>
