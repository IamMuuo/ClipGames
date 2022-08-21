// Demonstrates openning a window
#include <SFML/Graphics.hpp>
#include <SFML/Graphics/Color.hpp>
#include <SFML/Graphics/RectangleShape.hpp>
#include <SFML/Graphics/RenderWindow.hpp>
#include <SFML/System/Vector2.hpp>
#include <SFML/Window/Event.hpp>
#include <SFML/Window/VideoMode.hpp>

int main()
{
    sf::RenderWindow window (sf::VideoMode(640, 480), "First Window!");

    // crwating a rectangle
    sf::RectangleShape rectangle(sf::Vector2f(128.f, 128.f));
    rectangle.setFillColor(sf::Color::Red);
    rectangle.setPosition(320, 240);
    rectangle.setOrigin(rectangle.getSize().x/2, rectangle.getSize().y / 2);


    // game loop
    while(window.isOpen())
    {
        // process game
        // check for events ..
        sf::Event event;

        while(window.pollEvent(event)){
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }
        }

        // update game

        // render
        window.clear();
        window.draw(rectangle);
        window.display();
    }
}
