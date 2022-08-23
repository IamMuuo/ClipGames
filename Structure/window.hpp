#pragma once

#include <SFML/Graphics.hpp>

#include <SFML/Graphics/Drawable.hpp>
#include <SFML/Graphics/RenderWindow.hpp>
#include <SFML/System/Vector2.hpp>
#include <string>
class Window
{
public:
    Window();
    Window(const std::string& l_title, sf::Vector2i l_size);

    ~Window();

    void BeginDraw();	// clear the window
    void EndDraw();	// call display


    void update();

    bool isDone();
    bool isFullScreen();

    sf::Vector2i getWindowSize();

    void ToggleFullScreen();

    void Draw(sf::Drawable& l_drawable);

    void setFrameLimit(int8_t limit);

private:
    void setup(const std::string& l_title, sf::Vector2i l_size);

    void destroy();
    void create();

    sf::RenderWindow m_window;
    sf::Vector2i m_windowSize;
    std::string m_windowTitle;
    bool m_isDone;
    bool m_isFullScreen;
};

