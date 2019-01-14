# This file is part of Minke
# Copyright (c) 2019 Presteniko Septi Rahadian (presteniko@gmail.com)
# 
# Minke is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Minke is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY of FITNESS FOR A PARTICULAR PURPOSE . See the 
# GNU Affero General Public License for more details.
#
# A copy of the GNU Affero General Public License can be obtained at
# <http://www/gnu.org/licenses/>.

#TODO:
# 1. Handle file opener
# 2. Get Epub Metadata
# 3. Convert Metadata to templated JSON
# 4. Move all sentences based on delimiter ('.') into templated JSON designated spot
# 5. Export to file or move to database handler

import os
from ebooklib import epub

class Minke:
    # def __init__ (self, name, ext, size):
    #     self.name = name,
    #     self.ext = ext,
    #     self.size = size    
    
    def run (self):
        book = epub.read_epub('test.epub')
        print(book)
        print(book.get_metadata('DC', 'title'))
        # print(book.get_items())
        gen_items = book.get_items()
        for item in gen_items:
            print(item)
        

if __name__ == '__main__':
    Minke().run()