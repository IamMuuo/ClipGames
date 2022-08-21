// Demonstrates openning a window
#include <SFML/Graphics.hpp>
#include <SFML/Graphics/RenderWindow.hpp>
#include <SFML/Window/Event.hpp>
#include <SFML/Window/VideoMode.hpp>

int main()
{
    sf::RenderWindow window (sf::VideoMode(640, 480), "First Window!");

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
        // Draw sprites here ..
        window.display();
    }
}
