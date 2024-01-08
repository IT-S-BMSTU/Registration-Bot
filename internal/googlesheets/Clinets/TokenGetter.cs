﻿using DataBaseService.Protos;
using GoogleSheetsService.Backend;
using Grpc.Net.Client;

namespace GoogleSheetsService.Clients
{
    public class TokenGetter
    {
        public static async Task<string> GetGoogleApiSheetsToken(int bot_id, int owner)
        {
            Console.WriteLine(new ConfigManager().GetConnetionToDataBaseMicroserice());

            using (var channel = GrpcChannel.ForAddress(new ConfigManager().GetConnetionToDataBaseMicroserice()))
            {
                var clinet = new SheetConnector.SheetConnectorClient(channel);

                var token = await clinet.GetGoogleSheetsTokenAsync(new GetGoogleSheetsTokenRequest
                {
                    BotId = bot_id,
                    Owner = owner
                });

                return token.Token;

            }
        }

    }
}