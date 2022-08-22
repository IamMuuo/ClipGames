TEMPLATE = app
CONFIG += console c++17
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        game.cpp \
        main.cpp \
        window.cpp

LIBS += \
    /lib/libsfml-graphics.so\
    /lib/libsfml-window.so\
    /lib/libsfml-system.so\

HEADERS += \
    game.hpp \
    window.hpp
