MENU_PROMPT = 'Enter "c" to create blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit'

blogs = dict()  # blog_name : Blog object



def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually Exit
    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    # Print he avaia blogs
    for key, blog in blogs.items():
        print('- {}'.format(blog))
