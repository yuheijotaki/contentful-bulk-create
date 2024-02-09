import json
import time
import config
from contentful_management import Client
from contentful_management.errors import NotFoundError, BadRequestError  # エラーハンドリングのために必要なエラータイプをインポート

# CMAトークンとSpace IDの設定
cma_token = config.CMA_TOKEN
space_id = config.SPACE_ID
space_env = config.SPACE_ENVIRONMENT
content_model = config.CONTENT_MODEL

def create_article_entry(client, title):
    try:
        entry_attributes = {
            'content_type_id': content_model,
            'fields': {
                'title': {
                    'en-US': title,
                },
                # 'content': {
                #     'en-US': content,
                # },
            },
        }
        entry = client.entries(space_id, space_env).create("", entry_attributes)
        print(f'Article "{title}" has been created with ID: {entry.id}')

        # エントリーの公開
        entry.publish()
        print(f'Article "{title}" has been published with ID: {entry.id}')
    except BadRequestError as e:
        print(f'Error creating article "{title}": {e.message}')
    except NotFoundError as e:
        print(f'Error: {e.message}')

def bulk_create_articles(client, space_id, articles):
    for article_data in articles:
        title = article_data['title']
        # content = article_data['content']
        create_article_entry(client, title)
        time.sleep(1)  # API負荷軽減を目的とした1秒のインターバル

def main():
    # Contentfulへの接続
    client = Client(cma_token)

    # 記事データが格納されたjsonファイルを読み込む
    with open('articles.json', 'r', encoding='utf-8') as file:
        articles = json.load(file)

    # 記事を一括で登録
    bulk_create_articles(client, space_id, articles)

if __name__ == "__main__":
    main()
