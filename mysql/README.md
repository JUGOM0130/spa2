# macSQLServer環境構築
1. [こちら参考にしました](https://style.potepan.com/articles/19020.html)
2. Homebrewが入っているか
	=>入ってない場合入れましょう
```
brew --version
```
3. mysqlのinstall

```
brew install mysql
```
4. sqlserver起動

```
mysql.server start
```
5. Login

```
mysql -u root
```
6. sqlserver停止

```
mysql.server stop
```
7. Userの作成

```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

	* newuser = ユーザ名
	* localhost = どこからアクセスができるユーザか %にするとどこからでもアクセス可能 
	
```sql
GRANT ALL PRIVILEGES ON dbname.tablename TO 'newuser'@'localhost';
```
	* dbname = データベース名（アクセス可能な)
	* tablenama = テーブル名（アクセス可能な）
	
8. 設定の反映
```sql
FLUSH PRIVILEGES;
```