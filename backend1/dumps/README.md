# 別環境で環境を構築する
* DBの作成
    ```sql
    CREATE DATABASE a_system;
    ```
* アカウントの作成
    * adminというユーザを作成PW0000
    ```sql
    create user 'admin'@'localhost' identified by '0000'
    ```
    * adminにフル権限を付与(全DB.Table)
    ```sql
        grant all on *.* to admin
    ```
