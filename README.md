# Automating the Wikipedia Crawl

Whilst it's interesting to click through Wikipedia, it takes a lot of time to click through and read all those articles. We're going to work on automating this process, ending up with a program that will go through Wikipedia for us, keeping track of the first links on each page and seeing where they lead. In order to do this, we'll need to find out about how web pages work and get to know some of the Python tools we can use to interact with the web and web content.


# How do Web pages Work?
A program that interacts with websites is called a web crawler. Web crawlers are used to create search engine indexes, to archive pages, and in our case: to explore Wikipedia. In order to write a crawler we need to understand how web pages work. In particular, we need to know some HTML.

If you're an aspiring web developer, you're probably already familiar with HTML. If you aren't familiar with HTML, don't fret! You don't need to know much HTML to write a web crawler. Read on for an overview of the essentials.

HTML, or HyperText Markup Language, is the source code of web pages. An HTML document is a text document that describes what should be on a page. It includes text content, URLs for the images and videos that should be on the page, and information about how the content should be arranged and styled. Your web browser receives raw HTML and renders nicely formatted, multimedia web pages from it.


# Beautiful Soup

Now that we know how to make web requests and download html, it's time to see how we can parse HTML. Since HTML is simply text, we could parse through it with the tools we already know; loops and string methods. This would be challenging though, HTML is a very flexible language which makes it tricky to parse correctly. Fortunately past programmers have solved this problem for us.

# Recording our Progress
As we loop, we'll need to keep track of the articles we visit so we can output the path our crawler finds. I'll add this into our process:

1. Open an article
2. Find the first link in the article
3. Follow the link
4. Record the link in the article_chain data structure.
5. Repeat this process until we reach the Philosophy article, or get stuck in an article cycle.
