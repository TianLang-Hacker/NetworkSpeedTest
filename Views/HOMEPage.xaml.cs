using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;
using System.Diagnostics;
using System.IO;
using System.Threading.Tasks;

namespace Network_SpeedTest.Views;

public sealed partial class HOMEPage : Page
{
    public HOMEPage()
    {
        InitializeComponent();
    }

    private async void StartButton_Click(object sender, RoutedEventArgs e)
    {
        // 按下按钮后，启动加载动画
        loadingRing.IsActive = true;

        try
        {
            var programPath = @"E:\学期项目\Network SpeedTest\Py\dist\Speedtest.exe"; // 你的程序路径
            var workingDirectory = Path.GetDirectoryName(programPath);

            // 设置工作目录
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = programPath,
                WorkingDirectory = workingDirectory,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                CreateNoWindow = true
            };

            using var process = new Process { StartInfo = startInfo };
            process.Start();

            // 输出程序的标准输出，以便调试
            string output = process.StandardOutput.ReadToEnd();
            Debug.WriteLine(output);

            // 等待程序结束
            await process.WaitForExitAsync();

            // 检查 log 文件是否生成
            var logFilePath = Path.Combine(path1: workingDirectory, "Speedtest.log");
            if (File.Exists(logFilePath))
            {
                // 处理 log 文件，如果需要的话
                // ...
            }
        }
        finally
        {
            // 程序结束后，关闭加载动画
            loadingRing.IsActive = false;
        }
    }
}
