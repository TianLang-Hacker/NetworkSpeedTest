﻿using Microsoft.UI.Xaml;

using Network_SpeedTest.Contracts.Services;
using Network_SpeedTest.ViewModels;

namespace Network_SpeedTest.Activation;

public class DefaultActivationHandler : ActivationHandler<LaunchActivatedEventArgs>
{
    private readonly INavigationService _navigationService;

    public DefaultActivationHandler(INavigationService navigationService)
    {
        _navigationService = navigationService;
    }

    protected override bool CanHandleInternal(LaunchActivatedEventArgs args)
    {
        // None of the ActivationHandlers has handled the activation.
        return _navigationService.Frame?.Content == null;
    }

    protected async override Task HandleInternalAsync(LaunchActivatedEventArgs args)
    {
        _navigationService.NavigateTo(typeof(HOMEViewModel).FullName!, args.Arguments);

        await Task.CompletedTask;
    }
}
