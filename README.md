# 概要

ECサイトのサンプル

## フロントエンド

言語：TypeScript

フレームワーク：Vue

## バックエンド

言語:Python

フレームワーク：FastAPI

## データベース

PostgreSQL

# ローカルサーバの立て方

postgreSQL/FastAPI/vueを実行するためのローカルサーバを立てる

## postgreSQL

### サーバ起動

```sh
pg_ctl start
```

host:localhost

port:5432

### サーバ停止

```sh
pg_ctl stop
```

### サーバ状態の確認

```sh
pg_ctl status
```

## FastAPI

### 仮想環境

FastAPIではvenvで仮想環境を作っているので、activateにする

```sh
FastAPI_env/Scripts/activate
```

仮想環境を終了する時
```sh
deactivate
```

### サーバ起動

```sh
cd backend/
uvicorn main:app --reload
```
または
```sh
npm run api
```

http://127.0.0.1:8000/

## vue

### サーバ起動

```sh
cd frontend/
npm run dev
```
または
```sh
npm run vue
```

http://127.0.0.1:8080/

# Vue.jsについて

Vueの説明

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin) to make the TypeScript language service aware of `.vue` types.

If the standalone TypeScript plugin doesn't feel fast enough to you, Volar has also implemented a [Take Over Mode](https://github.com/johnsoncodehk/volar/discussions/471#discussioncomment-1361669) that is more performant. You can enable it by the following steps:

1. Disable the built-in TypeScript Extension
    1) Run `Extensions: Show Built-in Extensions` from VSCode's command palette
    2) Find `TypeScript and JavaScript Language Features`, right click and select `Disable (Workspace)`
2. Reload the VSCode window by running `Developer: Reload Window` from the command palette.

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```
