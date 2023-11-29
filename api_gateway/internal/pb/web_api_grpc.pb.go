// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.19.6
// source: proto/web_api.proto

package pb

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// DataSenderClient is the client API for DataSender service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type DataSenderClient interface {
	CreateBot(ctx context.Context, in *CreateBotRequest, opts ...grpc.CallOption) (*CreateBotResponse, error)
	TurnOnBot(ctx context.Context, in *TurnOnBotRequest, opts ...grpc.CallOption) (*BaseResponse, error)
	TurnOffBot(ctx context.Context, in *TurnOffBotRequest, opts ...grpc.CallOption) (*BaseResponse, error)
}

type dataSenderClient struct {
	cc grpc.ClientConnInterface
}

func NewDataSenderClient(cc grpc.ClientConnInterface) DataSenderClient {
	return &dataSenderClient{cc}
}

func (c *dataSenderClient) CreateBot(ctx context.Context, in *CreateBotRequest, opts ...grpc.CallOption) (*CreateBotResponse, error) {
	out := new(CreateBotResponse)
	err := c.cc.Invoke(ctx, "/DataSender/CreateBot", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *dataSenderClient) TurnOnBot(ctx context.Context, in *TurnOnBotRequest, opts ...grpc.CallOption) (*BaseResponse, error) {
	out := new(BaseResponse)
	err := c.cc.Invoke(ctx, "/DataSender/TurnOnBot", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *dataSenderClient) TurnOffBot(ctx context.Context, in *TurnOffBotRequest, opts ...grpc.CallOption) (*BaseResponse, error) {
	out := new(BaseResponse)
	err := c.cc.Invoke(ctx, "/DataSender/TurnOffBot", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DataSenderServer is the server API for DataSender service.
// All implementations should embed UnimplementedDataSenderServer
// for forward compatibility
type DataSenderServer interface {
	CreateBot(context.Context, *CreateBotRequest) (*CreateBotResponse, error)
	TurnOnBot(context.Context, *TurnOnBotRequest) (*BaseResponse, error)
	TurnOffBot(context.Context, *TurnOffBotRequest) (*BaseResponse, error)
}

// UnimplementedDataSenderServer should be embedded to have forward compatible implementations.
type UnimplementedDataSenderServer struct {
}

func (UnimplementedDataSenderServer) CreateBot(context.Context, *CreateBotRequest) (*CreateBotResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateBot not implemented")
}
func (UnimplementedDataSenderServer) TurnOnBot(context.Context, *TurnOnBotRequest) (*BaseResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method TurnOnBot not implemented")
}
func (UnimplementedDataSenderServer) TurnOffBot(context.Context, *TurnOffBotRequest) (*BaseResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method TurnOffBot not implemented")
}

// UnsafeDataSenderServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to DataSenderServer will
// result in compilation errors.
type UnsafeDataSenderServer interface {
	mustEmbedUnimplementedDataSenderServer()
}

func RegisterDataSenderServer(s grpc.ServiceRegistrar, srv DataSenderServer) {
	s.RegisterService(&DataSender_ServiceDesc, srv)
}

func _DataSender_CreateBot_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateBotRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DataSenderServer).CreateBot(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/DataSender/CreateBot",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DataSenderServer).CreateBot(ctx, req.(*CreateBotRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DataSender_TurnOnBot_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TurnOnBotRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DataSenderServer).TurnOnBot(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/DataSender/TurnOnBot",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DataSenderServer).TurnOnBot(ctx, req.(*TurnOnBotRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DataSender_TurnOffBot_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TurnOffBotRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DataSenderServer).TurnOffBot(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/DataSender/TurnOffBot",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DataSenderServer).TurnOffBot(ctx, req.(*TurnOffBotRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// DataSender_ServiceDesc is the grpc.ServiceDesc for DataSender service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var DataSender_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "DataSender",
	HandlerType: (*DataSenderServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateBot",
			Handler:    _DataSender_CreateBot_Handler,
		},
		{
			MethodName: "TurnOnBot",
			Handler:    _DataSender_TurnOnBot_Handler,
		},
		{
			MethodName: "TurnOffBot",
			Handler:    _DataSender_TurnOffBot_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "proto/web_api.proto",
}
