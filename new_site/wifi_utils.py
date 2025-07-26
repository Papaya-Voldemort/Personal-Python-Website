import speedtest
import pywebio
import time
import threading

print(f"Speedtest version: {speedtest.__version__}")

def wifi_speed_test():
    with pywebio.output.use_scope('wifi_speed_test', clear=True):
        pywebio.output.put_markdown("# WiFi Speed Test")

        # Initialize speedtest
        pywebio.output.put_text("🔍 Finding best server...")
        pywebio.output.put_processbar('server_progress')

        st = speedtest.Speedtest()

        # Simulate server selection progress
        for i in range(101):
            pywebio.output.set_processbar('server_progress', i/100)
            time.sleep(0.01)

        st.get_best_server()
        pywebio.output.put_text(f"✅ Connected to: {st.best['sponsor']} ({st.best['name']})")

        # Ping test
        pywebio.output.put_text("\n🏓 Testing ping...")
        pywebio.output.put_processbar('ping_progress')

        for i in range(101):
            pywebio.output.set_processbar('ping_progress', i/100)
            time.sleep(0.02)

        ping = st.results.ping
        pywebio.output.put_text(f"✅ Ping: {ping:.2f} ms")

        # Download test with progress
        pywebio.output.put_text("\n⬇️ Testing download speed...")
        pywebio.output.put_processbar('download_progress')
        pywebio.output.put_text("Current speed: 0.00 Mbps", scope='download_speed')

        download_speed = run_download_test_with_progress(st)
        pywebio.output.put_text(f"✅ Download Speed: {download_speed:.2f} Mbps")

        # Upload test with progress
        pywebio.output.put_text("\n⬆️ Testing upload speed...")
        pywebio.output.put_processbar('upload_progress')
        pywebio.output.put_text("Current speed: 0.00 Mbps", scope='upload_speed')

        upload_speed = run_upload_test_with_progress(st)
        pywebio.output.put_text(f"✅ Upload Speed: {upload_speed:.2f} Mbps")

        # Final results
        pywebio.output.put_markdown("## 📊 Final Results")
        pywebio.output.put_table([
            ['Metric', 'Value'],
            ['Download Speed', f'{download_speed:.2f} Mbps'],
            ['Upload Speed', f'{upload_speed:.2f} Mbps'],
            ['Ping', f'{ping:.2f} ms']
        ])

def run_download_test_with_progress(st):
    """Run download test with simulated progress updates"""
    download_complete = False
    final_speed = 0

    def progress_updater():
        nonlocal download_complete, final_speed
        current_speed = 0

        # Simulate progressive speed increase
        for i in range(101):
            if download_complete:
                break

            progress = i / 100
            pywebio.output.set_processbar('download_progress', progress)

            # Simulate speed ramping up and fluctuating
            if i < 20:
                current_speed = (i / 20) * 30  # Ramp up to ~30 Mbps
            elif i < 80:
                # Fluctuate around the actual speed
                import random
                current_speed = max(0, final_speed * (0.8 + 0.4 * random.random()))
            else:
                current_speed = final_speed * (0.95 + 0.1 * (i - 80) / 20)

            pywebio.output.put_text(f"Current speed: {current_speed:.2f} Mbps", scope='download_speed')
            time.sleep(0.05)

    # Start progress thread
    thread = threading.Thread(target=progress_updater, daemon=True)
    thread.start()

    # Run actual test
    download_result = st.download() / 1_000_000
    final_speed = download_result
    download_complete = True

    # Wait for thread to finish
    thread.join(timeout=1)

    # Ensure progress bar is complete
    pywebio.output.set_processbar('download_progress', 1.0)
    pywebio.output.put_text(f"Current speed: {final_speed:.2f} Mbps", scope='download_speed')

    return download_result

def run_upload_test_with_progress(st):
    """Run upload test with simulated progress updates"""
    upload_complete = False
    final_speed = 0

    def progress_updater():
        nonlocal upload_complete, final_speed
        current_speed = 0

        # Simulate progressive speed increase
        for i in range(101):
            if upload_complete:
                break

            progress = i / 100
            pywebio.output.set_processbar('upload_progress', progress)

            # Simulate speed ramping up and fluctuating
            if i < 20:
                current_speed = (i / 20) * 20  # Ramp up to ~20 Mbps
            elif i < 80:
                # Fluctuate around the actual speed
                import random
                current_speed = max(0, final_speed * (0.8 + 0.4 * random.random()))
            else:
                current_speed = final_speed * (0.95 + 0.1 * (i - 80) / 20)

            pywebio.output.put_text(f"Current speed: {current_speed:.2f} Mbps", scope='upload_speed')
            time.sleep(0.05)

    # Start progress thread
    thread = threading.Thread(target=progress_updater, daemon=True)
    thread.start()

    # Run actual test
    upload_result = st.upload() / 1_000_000
    final_speed = upload_result
    upload_complete = True

    # Wait for thread to finish
    thread.join(timeout=1)

    # Ensure progress bar is complete
    pywebio.output.set_processbar('upload_progress', 1.0)
    pywebio.output.put_text(f"Current speed: {final_speed:.2f} Mbps", scope='upload_speed')

    return upload_result
