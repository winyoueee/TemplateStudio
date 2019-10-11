﻿using System;
using System.Windows.Controls;

namespace Param_RootNamespace.Contracts.Services
{
    public interface INavigationService
    {
        event EventHandler<string> Navigated;

        bool CanGoBack { get; }

        void Initialize(Frame shellFrame);

        bool Navigate(string pageKey, object parameter = null, bool clearNavigation = false);

        void GoBack();
    }
}
