using Microsoft.UI.Xaml.Controls;

using Network_SpeedTest.ViewModels;

namespace Network_SpeedTest.Views;

public sealed partial class MainPage : Page
{
    public MainViewModel ViewModel
    {
        get;
    }

    public MainPage()
    {
        ViewModel = App.GetService<MainViewModel>();
        InitializeComponent();
    }
}
