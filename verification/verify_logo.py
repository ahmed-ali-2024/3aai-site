from playwright.sync_api import sync_playwright

def verify_logo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("http://localhost:3000")
            page.wait_for_selector("img[alt='3A-AI Logo']")
            
            # Screenshot Navbar
            page.screenshot(path="verification/logo_navbar.png")
            
            # Screenshot Vision
            page.locator("#vision").scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            page.screenshot(path="verification/logo_vision.png")
            
            # Screenshot Footer
            page.locator("#contact").scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            page.screenshot(path="verification/logo_footer.png")
            
            print("Screenshots taken.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_logo()
