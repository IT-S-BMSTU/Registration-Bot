import asyncio

import micro_services.ApiGateWay.web_api_rpc.web_api_pb2 as pb2
import micro_services.ApiGateWay.web_api_rpc.web_api_pb2_grpc as p2b_grpc
import micro_services.ApiGateWay.clients.bot.bot_client as bot
from telegram_bot.bot_launcher import run_instance

## @brief Класс описывающий объект сервиса - входной точки для фронтенда.
class DataSenderService(p2b_grpc.DataSenderServicer):
    ## @brief Функция создания нового бота.
    # @param self Объект класса 
    # @param request Запрос, посылемый с фронтенда, имеет тип данных CreateBotRequest описан в bot.proto
    # @param context Серверный контекст, понятие не имею зачем нужно 
    # @return Ответ сервера, CreateBotResponse описан в bot.proto
    # @see bot_client.create_new_bot_asker()
    
    async def Create_Bot(self, request, context):
        print('Create new Bot Request')

        try:
            resp = await bot.create_new_bot_asker(user_id=request.from_user, journal=request.journal,
                                                  tg_token=request.tg_token,
                                                  sheets_token=request.sheets_token, start_msg=request.start_message,
                                                  end_msg=request.end_message)
            await run_instance(resp.bot_id)
            return resp
        except Exception as ex:
            return None