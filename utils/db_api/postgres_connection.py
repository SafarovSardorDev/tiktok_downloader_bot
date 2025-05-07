from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config

class Database:
    def __init__(self) -> None:
        self.pool : Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user = config.DB_USER,
            password = config.DB_PASS,
            host = config.DB_HOST,
            database = config.DB_NAME 
        )
    async def execute(self, command, *args,
                      
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection  
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
        return result
    

    async def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Users(
                id SERIAL PRIMARY KEY,
                telegram_id BIGINT NOT NULL UNIQUE,
                username VARCHAR(255) NULL
            );
        """
        await self.execute(sql, execute=True)
    
    async def check_new_user(self, telegram_id):
        sql = "SELECT * FROM Users WHERE telegram_id = $1"
        return await self.execute(sql, telegram_id, fetchrow=True)
    
    async def add_user(self, telegram_id, username):

        sql = """
        INSERT INTO Users(telegram_id, username) VALUES($1, $2) returning *
        """
        return await self.execute(sql, telegram_id, username, fetchrow=True)

    async def all_users(self):
        sql = 'SELECT * FROM Users;'

        return await self.execute(sql, fetch=True)
    
    # async def get_one_user(self, telegram_id):
    #     sql = "SELECT * FROM Users WHERE telegram_id = $1;"
    #     return await self.execute(sql, telegram_id, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users;"
        return await self.execute(sql, fetchval=True)


            
                
