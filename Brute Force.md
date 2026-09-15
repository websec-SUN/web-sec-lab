# DVWA Brute Force Low 暴力破解
## 环境信息
- 靶场：DVWA
- 漏洞模块：Brute Force（暴力破解）
- 安全等级：Low
- 漏洞原理：后端没有做任何防暴力破解措施，没有验证码、没有登录失败锁定；直接把GET参数`username`和`password`拼入SQL查询，可直接暴力破解账号密码。
## 源码分析
```php
<?php
if( isset( $_GET[ 'Login' ] ) ) {
    // 获取用户输入
    $user = $_GET[ 'username' ];
    $pass = $_GET[ 'password' ];
    $pass = md5( $pass );
    // 直接拼接SQL语句
    $query  = "SELECT * FROM users WHERE user = '$user' AND password = '$pass';";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
    if ($result && mysqli_num_rows($result) == 1 ) {
        echo "<p>Welcome to the password protected area admin</p>";
    } else {
        echo "<pre><br>Username and/or password incorrect.</pre>";
    }
}
?>

## 文件2：DVWA-Brute-Force-Medium.md
```markdown
# DVWA Brute Force Medium 暴力破解

## 环境信息
- 靶场：DVWA
- 漏洞模块：Brute Force（暴力破解）
- 安全等级：Medium
- 漏洞原理：增加了简单延迟防护，登录错误后sleep 2秒，增加爆破耗时；但是**没有验证码、没有账号锁定**，依然可以暴力破解。

## 源码分析
```php
<?php
if( isset( $_GET[ 'Login' ] ) ) {
    $user = $_GET[ 'username' ];
    $pass = $_GET[ 'password' ];

    $pass = md5( $pass );

    $query  = "SELECT * FROM users WHERE user = '$user' AND password = '$pass';";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

    if ($result && mysqli_num_rows($result) == 1 ) {
        echo "<p>Welcome to the password protected area admin</p>";
    } else {
        // 登录失败，sleep 2秒，拖慢爆破速度
        sleep(2);
        echo "<pre><br>Username and/or password incorrect.</pre>";
    }
}
?>
