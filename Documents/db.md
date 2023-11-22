# データベースの確認

## sqlに入る

```
docker compose exec db psql -d database
```
## テーブル一覧

```
\dt
```

## テーブルの中身の確認方法

```
select * ftom users;
select * ftom post;
select * ftom image;
```

## データベースの更新

```
docker compose exec app flask db migrate

docker compose exec app flask db upgrade
```