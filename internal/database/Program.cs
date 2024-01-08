using DataBaseService.Backend.Config;
using DataBaseService.Clients;
using DataBaseService.Services.bot;
using DataBaseService.Services.Bot;
using DataBaseService.Services.SheetConnector;
using DataBaseService.Services.User;
using System.Net.WebSockets;

var builder = WebApplication.CreateBuilder(args);

// Additional configuration is required to successfully run gRPC on macOS.
// For instructions on how to configure Kestrel and gRPC clients on macOS, visit https://go.microsoft.com/fwlink/?linkid=2099682

// Add services to the container.
builder.Services.AddGrpc();

var app = builder.Build();

// Configure the HTTP request pipeline.




app.MapGrpcService<BotGetterService>();
app.MapGrpcService<BotWorkerService>();

app.MapGrpcService<UserWorkerService>();

app.MapGrpcService<SheetConnetService>();

app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
