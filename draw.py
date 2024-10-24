import pygame
import sys
import os
import base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def draw_and_save():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Whiteboard")

    # Create a separate surface for drawing
    drawing_surface = pygame.Surface((width, height))

    # Set up colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Fill the drawing surface with white
    drawing_surface.fill(WHITE)

    # Create a font for the button text
    font = pygame.font.Font(None, 36)

    # Create a button
    button_rect = pygame.Rect(10, 10, 200, 50)
    button_text = font.render("Send to API", True, BLACK)
    button_text_rect = button_text.get_rect(center=button_rect.center)

    # Main drawing loop
    drawing = False
    last_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    # Save the drawing and process it
                    pygame.image.save(drawing_surface, "temp_drawing.png")
                    process_image("temp_drawing.png")
                else:
                    drawing = True
                    last_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.MOUSEMOTION and drawing:
                if last_pos:
                    pygame.draw.line(drawing_surface, BLACK, last_pos, event.pos, 2)
                    last_pos = event.pos
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    # Save the drawing when 'S' is pressed
                    pygame.image.save(drawing_surface, "temp_drawing.png")
                    pygame.quit()
                    return "temp_drawing.png"

        # Clear the main screen
        screen.fill(WHITE)

        # Blit the drawing surface onto the main screen
        screen.blit(drawing_surface, (0, 0))

        # Draw the button on the main screen
        pygame.draw.rect(screen, RED, button_rect)
        screen.blit(button_text, button_text_rect)

        # Update the display
        pygame.display.flip()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def process_image(image_path):
    print(f"Processing image: {image_path}")
    
    # Encode the image
    base64_image = encode_image(image_path)

    # Initialize Groq client
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    # Send request to Groq API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is in this drawing?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="llama-3.2-90b-vision-preview",
    )

    # Print the API response
    print(chat_completion.choices[0].message.content)

    # Remove the temporary file
    os.remove(image_path)

if __name__ == "__main__":
    saved_image = draw_and_save()
    if saved_image:
        process_image(saved_image)
