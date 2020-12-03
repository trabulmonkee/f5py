# -*- coding: utf-8 -*-

class TestDynamicContent:

    URL = 'https://the-internet.herokuapp.com/dynamic_content'

    def test_one_10_char_word(self, driver):
        driver.get(self.URL)  # navigate to specified url
        bool = False # initial start value, default test failure is assumed
        # get all lorem ipsum text elements on current page
        lorem_text_objects = driver.find_elements_by_css_selector('div#content div.row div.large-10')
        # iterate through each image object, to get src attribute
        for item in lorem_text_objects:
            # get the text attribute of the current item object
            # clean up whitespace (strip)
            # split on the space ' ' character
            split_text = item.text.strip().split(' ')
            # iterate through the text list, to test each word length
            for t in split_text:
                # is current word length greater than or equal to 10
                if len(t) >= 10:
                    bool = True
                    break # break out of inner for loop (words)
            if bool:
                break # break out of outer for loop (text objects)

        assert bool, "expected lorem ipsum text block at least 10 char word was not found"

    def test_one_stretch_goal(self, driver):
        driver.get(self.URL)  # navigate to specified url
        # get the full page text
        page_text = driver.find_element_by_tag_name('body').text
        # split words in the text on the space ' ' char
        split_text = page_text.strip().split(' ')
        cur_len = 0  # initial start value
        longest_word = ''  # initial start value
        # iterate through the text list, to test each word length
        for t in split_text:
            if len(t) > cur_len:
                cur_len = len(t)
                longest_word = t

        # failing on purpose to see print messages of the longest word
        msg = "failing on purpose, longest word: {0}, with length {1}".format(longest_word, cur_len)
        print(msg) # to stdout
        assert False, msg

    def test_two_punisher(self, driver):
        driver.get(self.URL)  # navigate to specified url
        bool = True  # initial start value, default test pass if punisher avatar image is not found
        # get all avatar image elements on current page
        image_objects = driver.find_elements_by_css_selector('div#content div.row div.large-2 img')
        # iterate through each image object, to get src attribute
        for obj in image_objects:
            # get the current image object src attribute
            img_src = obj.get_attribute("src")
            # image src name check, if image 3 then it is the punisher avatar image
            # change bool to false, test failure because punisher image was found
            if 'avatar-3.jpg' in img_src.lower():
                bool = False
                break # break for loop no longer need to process because punisher image was found

        assert bool, "unexpected punisher image was found"

    def test_two_stretch_goal(self, driver):
        driver.get(self.URL)  # navigate to specified url
        # build json object of available image numbers to names
        # see: https://github.com/saucelabs/the-internet/tree/master/public/img/avatars
        image_names = {
            '1': 'mario',
            '2': 'boba fett',
            '3': 'punisher',
            '5': 'wolverine',
            '6': 'stormtrooper',
            '7': 'harley quinn'
        }
        msg = 'failing on purpose\n'
        # get all avatar image elements on current page
        image_objects = driver.find_elements_by_css_selector('div#content div.row div.large-2 img')
        # iterate through each image object, to get/print image name
        for obj in image_objects:
            # get the src attribute of current image object
            # split on the dash '-' character
            # get the last element of the list
            # split on the period '.' character
            # get the first element of the list
            img_num = obj.get_attribute("src").split('-')[-1].split('.')[0]
            msg = msg + "{0} image found\n".format(image_names[img_num])

        print(msg) # to stdout
        # failing on purpose to see print messages of the dynamic avatar images on the page
        assert False, msg