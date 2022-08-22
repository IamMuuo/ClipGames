#include "window.hpp"
#include <SFML/System/Vector2.hpp>
#include <SFML/Window/Event.hpp>
#include <string>

Window::Window()
{
    setup("Window",sf::Vector2i(640, 480));
}

Window::Window(const std::string& l_title,sf::Vector2i l_size)
{
    setup(l_title, l_size);
}


Window::~Window(){destroy();}

void Window::setup(const std::string& l_title,
                   sf::Vector2i l_size)
{
    m_windowTitle = l_title;
    m_windowSize = l_size;
    m_isFullScreen = false;
    m_isDone = false;

    create();
}

void Window::create()
{
    // creates a window
    auto style = (m_isFullScreen ? sf::Style::Fullscreen : sf::Style::Default);

    m_window.create({m_windowSize.x, m_windowSize.y, 32},m_windowTitle, style);
}

void Window::destroy()
{
    m_window.close();
}

void Window::update()
{
    sf::Event event;

    while(m_window.pollEvent(event)){
        if(event.type == sf::Event::Closed)
        {
            m_isDone = true;
        }
        else if(event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::F)
        {
            ToggleFullScreen();
        }
    }
}

void Window::ToggleFullScreen()
{
    m_isFullScreen = !m_isFullScreen;
    destroy();
    create();
}

void Window::BeginDraw(){m_window.clear(sf::Color::Black);}

void Window::EndDraw(){m_window.display();}

void Window::Draw(sf::Drawable &l_drawable)
{
    m_window.draw(l_drawable);
}

bool Window::isDone()
{
    return m_isDone;
}
