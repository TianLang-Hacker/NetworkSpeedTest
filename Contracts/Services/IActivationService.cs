namespace Network_SpeedTest.Contracts.Services;

public interface IActivationService
{
    Task ActivateAsync(object activationArgs);
}
