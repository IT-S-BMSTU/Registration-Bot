// Code generated by mockery v2.36.1. DO NOT EDIT.

package mocks

import (
	domain "Registration-Bot/internal/domain"

	mock "github.com/stretchr/testify/mock"
)

// Repository is an autogenerated mock type for the Repository type
type Repository struct {
	mock.Mock
}

// AddBot provides a mock function with given fields: botID, journal, final
func (_m *Repository) AddBot(botID int, journal map[int]domain.Module, final string) error {
	ret := _m.Called(botID, journal, final)

	var r0 error
	if rf, ok := ret.Get(0).(func(int, map[int]domain.Module, string) error); ok {
		r0 = rf(botID, journal, final)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// GetCurrentModule provides a mock function with given fields: botID, chatID
func (_m *Repository) GetCurrentModule(botID int, chatID int64) (domain.Module, error) {
	ret := _m.Called(botID, chatID)

	var r0 domain.Module
	var r1 error
	if rf, ok := ret.Get(0).(func(int, int64) (domain.Module, error)); ok {
		return rf(botID, chatID)
	}
	if rf, ok := ret.Get(0).(func(int, int64) domain.Module); ok {
		r0 = rf(botID, chatID)
	} else {
		r0 = ret.Get(0).(domain.Module)
	}

	if rf, ok := ret.Get(1).(func(int, int64) error); ok {
		r1 = rf(botID, chatID)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// GetFinal provides a mock function with given fields: botID
func (_m *Repository) GetFinal(botID int) (string, error) {
	ret := _m.Called(botID)

	var r0 string
	var r1 error
	if rf, ok := ret.Get(0).(func(int) (string, error)); ok {
		return rf(botID)
	}
	if rf, ok := ret.Get(0).(func(int) string); ok {
		r0 = rf(botID)
	} else {
		r0 = ret.Get(0).(string)
	}

	if rf, ok := ret.Get(1).(func(int) error); ok {
		r1 = rf(botID)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// GetState provides a mock function with given fields: botID, chatID
func (_m *Repository) GetState(botID int, chatID int64) (domain.State, error) {
	ret := _m.Called(botID, chatID)

	var r0 domain.State
	var r1 error
	if rf, ok := ret.Get(0).(func(int, int64) (domain.State, error)); ok {
		return rf(botID, chatID)
	}
	if rf, ok := ret.Get(0).(func(int, int64) domain.State); ok {
		r0 = rf(botID, chatID)
	} else {
		r0 = ret.Get(0).(domain.State)
	}

	if rf, ok := ret.Get(1).(func(int, int64) error); ok {
		r1 = rf(botID, chatID)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// SaveAnswer provides a mock function with given fields: botID, chatID, text
func (_m *Repository) SaveAnswer(botID int, chatID int64, text string) error {
	ret := _m.Called(botID, chatID, text)

	var r0 error
	if rf, ok := ret.Get(0).(func(int, int64, string) error); ok {
		r0 = rf(botID, chatID, text)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// SetModuleID provides a mock function with given fields: botID, chatID, questionID
func (_m *Repository) SetModuleID(botID int, chatID int64, questionID int) error {
	ret := _m.Called(botID, chatID, questionID)

	var r0 error
	if rf, ok := ret.Get(0).(func(int, int64, int) error); ok {
		r0 = rf(botID, chatID, questionID)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// SetStage provides a mock function with given fields: botID, chatID, stage
func (_m *Repository) SetStage(botID int, chatID int64, stage int) error {
	ret := _m.Called(botID, chatID, stage)

	var r0 error
	if rf, ok := ret.Get(0).(func(int, int64, int) error); ok {
		r0 = rf(botID, chatID, stage)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// SetState provides a mock function with given fields: botID, chatID, st
func (_m *Repository) SetState(botID int, chatID int64, st domain.State) error {
	ret := _m.Called(botID, chatID, st)

	var r0 error
	if rf, ok := ret.Get(0).(func(int, int64, domain.State) error); ok {
		r0 = rf(botID, chatID, st)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// NewRepository creates a new instance of Repository. It also registers a testing interface on the mock and a cleanup function to assert the mocks expectations.
// The first argument is typically a *testing.T value.
func NewRepository(t interface {
	mock.TestingT
	Cleanup(func())
}) *Repository {
	mock := &Repository{}
	mock.Mock.Test(t)

	t.Cleanup(func() { mock.AssertExpectations(t) })

	return mock
}
